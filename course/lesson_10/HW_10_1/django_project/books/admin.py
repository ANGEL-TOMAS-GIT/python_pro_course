from django.contrib import admin
from .models import Book, Category


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "price", "stock", "is_available")
    list_filter = ("author", "published_at")
    search_fields = ("title", "description", "author__username")
    ordering = ("-price",)


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInline]
