from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'bookclub/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'bookclub/book_detail.html'
    context_object_name = 'book'
