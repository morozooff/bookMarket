from django.urls import path
from .views import *


urlpatterns = [
    path('catalog/', BookListView.as_view(), name = 'market-catalog'),
    path('about/', about, name = 'market-about'),
    path('book/<int:pk>/', BookDetailView.as_view(), name = 'book-detail'),
    path('author/<str:name>/', AuthorBookListView.as_view(), name = 'author-books'),
    path('search/', book_search, name = 'market-search'),
    path('search_results/<str:query>/', SearchResultListView.as_view(), name = 'search-results'),
]
