from django.urls import path

from books.views import BookListView, CreateBookView, BookDetailView, UpdateBookView, DeleteBookView, AuthorListView, \
    CreateAuthorView, AuthorDetailView, UpdateAuthorView, DeleteAuthorView
from hollymovies_5.views import HomeView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='hollymovies_5'),
    path('books/', BookListView.as_view(), name='books'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('book/create/', CreateBookView.as_view(), name='create_book'),
    path('author/create/', CreateAuthorView.as_view(), name='create_author'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book/update/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('author/update/<int:pk>/', UpdateAuthorView.as_view(), name='update_author'),
    path('book/delete/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path('author/delete/<int:pk>/', DeleteAuthorView.as_view(), name='delete_author'),
    path('contact/', ContactView.as_view(), name='contact'),
]
