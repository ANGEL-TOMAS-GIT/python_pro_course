from django.contrib import admin
from .models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "book_author", "author", "published_at", "price", "stock", "is_available", "description", "photo")
    list_filter = ("author", "published_at")
    search_fields = ("title",)
    ordering = ("author",)


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInline]
