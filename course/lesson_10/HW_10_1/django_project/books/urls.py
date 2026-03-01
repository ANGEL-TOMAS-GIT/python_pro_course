from django.urls import path
from .views import books, home

urlpatterns = [
    path('', home, name="home"),
    path('book/', books, name="books"),
    
]
