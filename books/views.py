from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from books.forms import BookForm
from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = Book.objects.all()
        search = self.request.GET.get("search")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search)
            )

        status = self.request.GET.get("status")
        if status:
            queryset = queryset.filter(status=status)

        return queryset


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/create_book.html"
    success_url = reverse_lazy("book-list")


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/edit_book.html"
    success_url = reverse_lazy("book-list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/delete_book.html"
    success_url = reverse_lazy("book-list")