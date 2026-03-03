from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q


def home(request):
    return render(request, "index.html", {'title': "Home"})


def books(request):
    query = request.GET.get("q", "")
    all_books = Book.objects.all()
    
    if query:
        all_books = all_books.filter(
            Q(title__icontains=query) |
            Q(book_author__icontains=query)
        )
    
    return render(request, "book.html", {
        "books": all_books,
        "query": query,
        "empty": not all_books.exists()
    })


def description(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "description.html", {"book": book})
