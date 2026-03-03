from django.urls import path
from .views import home, books, description

urlpatterns = [
    path('', home, name="home"),
    path('book/', books, name="books"),
    path('book/<int:pk>/', description, name="book_detail"),

]
