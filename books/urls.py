from django.urls import path
from books.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("add/", BookCreateView.as_view(), name="book-add"),
    path("<int:pk>/edit/", BookUpdateView.as_view(), name="book-edit"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]