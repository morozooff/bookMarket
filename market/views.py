from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.forms.models import model_to_dict

from .forms import SearchBookForm
from order.forms import BasketAddBookForm
from .models import *

def home(request):
    return render(request, 'market/home.html')

def about(request):
    return render(request, 'market/about.html')


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

    def get_context_data(self, **kwargs):
        context = super(AuthorBookListView, self).get_context_data(**kwargs)
        author = get_object_or_404(Author, name=self.kwargs.get('name'))
        author_data = model_to_dict(author)
        context['author_name'] = author_data['name']
        context['author_biography'] = author_data['biography']
        context['author_avatar'] = author.avatar.url
        return context


class BookDetailView(FormMixin, DetailView):
    model = Book
    template_name = 'market/book_detail.html'
    form_class = BasketAddBookForm

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['form'] = BasketAddBookForm(initial = {'book': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BookDetailView, self).form_valid(form)


def book_search(request):
    if request.method == 'POST':
        form = SearchBookForm(request.POST)

        if form.is_valid():
            query = form.cleaned_data.get('search_request')
            return redirect('search-results', query)

    else:
        form = SearchBookForm()

    return render(request, 'market/search.html', {'form': form})


class SearchResultListView(ListView):
    model = Book
    template_name = 'market/search_results.html'
    context_object_name = 'books'
    ordering = ['name']

    def get_queryset(self):
        query = self.kwargs.get('query')

        authors_matches = Author.objects.filter(Q(name__icontains = query))
        ids = []
        author_id_relation = authors_matches.values('id')
        for author in author_id_relation:
            ids.append(author['id'])

        books_on_author = Book.objects.filter(Q(author__id__in = ids ))
        books_on_tags_and_name = Book.objects.filter(Q(name__icontains=query)|Q(tags__icontains = query))

        books_on_search_query = set(books_on_author | books_on_tags_and_name)

        return books_on_search_query




