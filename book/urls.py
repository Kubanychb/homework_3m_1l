from django.urls import path, include
from . import views

app_name = 'book'
urlpatterns = [
    path('book/', views.BookListView.as_view(), name='book_all'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),

]
