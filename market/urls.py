from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from .views import *

router = SimpleRouter()

# router.register('catalog', BookViewSet)

urlpatterns = router.urls

# urlpatterns += [path('registration', RegisterUserView.as_view())]

urlpatterns += [path('', home, name = 'market-home')]
urlpatterns += [path('catalog/', catalog, name = 'market-catalog')]
urlpatterns += [path('about/', about, name = 'market-about')]