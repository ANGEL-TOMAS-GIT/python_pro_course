from .models import Book
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


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
                Q(title__icontains=query) |
                Q(book_author__icontains=query) |
                Q(category__name__icontains=query)
            )
        
        return qs


class BooksListView(BaseBooksListView):
    template_name = "books.html"


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
