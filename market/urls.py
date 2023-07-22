from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from .views import *

router = SimpleRouter()

# router.register('catalog', BookViewSet)

urlpatterns = router.urls

# urlpatterns += [path('registration', RegisterUserView.as_view())]

urlpatterns += [path('', home, name = 'market-home')]
urlpatterns += [path('catalog/', BookListView.as_view(), name = 'market-catalog')]
urlpatterns += [path('about/', about, name = 'market-about')]
urlpatterns += [path('book/<int:pk>/', BookDetailView.as_view(), name = 'book-detail')]
urlpatterns += [path('author/<str:name>/', AuthorBookListView.as_view(), name = 'author-books')]