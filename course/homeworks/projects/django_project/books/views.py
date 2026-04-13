from .models import Book, Customer
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.orders.models import Order, OrderItem
from books.cart.cart import Cart
from django.contrib import messages
from books.forms import OrderCreateForm


class HomePageTemplateView(TemplateView):
    template_name = "index.html"


class BaseBooksListView(ListView):
    model = Book
    context_object_name = "books"
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(book_author__icontains=query) |
                Q(category__name__icontains=query)
            )
        
        return qs


class BooksListView(BaseBooksListView):
    template_name = "book_list.html"


class ManageBookListView(BaseBooksListView):
    template_name = "manage_books.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_description.html"


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = "__all__"
    template_name = "book_create.html"
    permission_required = 'books.add_book'
    raise_exception = True
    
    def get_success_url(self):
        return reverse_lazy('books')


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = "__all__"
    template_name_suffix = "_update_form"
    template_name = "book_update.html"
    permission_required = 'books.update_book'
    raise_exception = True
    
    def get_success_url(self):
        return reverse_lazy('books')


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    permission_required = 'books.delete_book'
    raise_exception = True
    
    success_url = reverse_lazy('books')


class CartDetailView(TemplateView):
    template_name = "cart/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        
        context["cart"] = cart
        context["total_price"] = cart.get_total_price()
        return context


class CartAddView(View):
    
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Book, pk=pk, is_active=True)
        quantity = int(request.POST.get("quantity", 1))
        cart.add(
            product=product,
            override_quantity=True,
            quantity=quantity,
        
        )
        messages.success(request, f"{product.title} added to cart")
        return redirect("cart_detail")


class CartRemoveView(View):
    
    def get(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Book, pk=pk, is_active=True)
        cart.remove(product)
        messages.info(request, f'{product.title} removed from the cart')
        return redirect("cart_detail")


class OrderCreateView(View):
    template_name = "order/create_order.html"
    
    def get(self, request):
        cart = Cart(request)
        
        initial = {}
        
        if request.user.is_authenticated:
            user = request.user
            
            initial = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
            
            customer = hasattr(user, "customer")
            
            if customer:
                initial.update({
                    "phone": getattr(customer, "phone", ""),
                    "address": getattr(customer, "address", "")
                })
        
        form = OrderCreateForm(initial=initial)
        
        context = {
            "form": form,
            "cart": cart,
            "total_price": cart.get_total_price()
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        cart = Cart(request)
        
        if not cart.cart:
            messages.warning(request, "The Cart is Empty!!")
            return redirect("cart_detail")
        
        form = OrderCreateForm(request.POST)
        
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = cart.get_total_price()
            
            if request.user.is_authenticated:
                customer, _ = Customer.objects.get_or_create(user=request.user)
                order.customer = customer
            
            order.save()
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"]
                )
            
            cart.clear()
            
            messages.success(
                request,
                f"The Order #{order.id} successfully completed"
            )
            
            return render(
                request,
                "order/success_order.html",
                {"order": order}
            )
        
        context = {
            "form": form,
            "cart": cart,
            "total_price": cart.get_total_price()
        }
        
        return render(request, self.template_name, context)
