from django.urls import path, include
from . import views
urlpatterns = [
    path('book/', views.book_all, name='book_all'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('add-book/', views.add_book, name='add_book'),
]
