
from django.shortcuts import render, get_object_or_404
from .serializers import *

from django.views.generic import ListView, DetailView


def catalog(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'market/catalog.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'market/catalog.html'
    context_object_name = 'books'
    ordering = ['name']
    paginate_by = 5


class AuthorBookListView(ListView):
    model = Book
    template_name = 'market/author_books.html'
    context_object_name = 'books'
    ordering = ['name']
    paginate_by = 5

    def get_queryset(self):
        author = get_object_or_404(Author,name = self.kwargs.get('name'))
        return Book.objects.filter(author = author)

class BookDetailView(DetailView):
    model = Book
    # template_name = 'market/book_detail.html'


def about(request):
    return render(request, 'market/about.html', {'title': 'О магазине TolStore'})


def home(request):
    return render(request, 'market/home.html')

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


