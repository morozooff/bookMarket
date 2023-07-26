from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket_detail, name = 'basket_detail'),
    path('basket-add/<int:book_id>', views.basket_add, name = 'basket_add'),
    path('basket-remove/<int:book_id>', views.basket_remove, name = 'basket_remove'),
    path('create', views.order_create, name = 'order_create'),
    path('created', views.order_create, name = 'order_created'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name = "order_detail"),
    path('my_orders/<int:pk>/', views.UserOrderListView.as_view(), name = "my_orders")
]