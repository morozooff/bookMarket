from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket_detail, name = 'basket_detail'),
    path('basket-add/<int:book_id>', views.basket_add, name = 'basket_add'),
    path('basket-remove/<int:book_id>', views.basket_remove, name = 'basket_remove'),
]