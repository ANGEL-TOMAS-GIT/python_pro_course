from django.shortcuts import render

# Create your views here.


from .models import Book


def home(request):
    return render(request, "index.html", {'title': "Home"})


def books(request):
    return render(request, "book.html", {'books': Book.objects.all()})
