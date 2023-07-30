from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket_detail, name = 'basket-detail'),
    path('basket-add/<int:book_id>', views.basket_add, name = 'basket-add'),
    path('basket-remove/<int:book_id>', views.basket_remove, name = 'basket-remove'),
    path('create', views.order_create, name = 'order-create'),
    path('created', views.order_create, name = 'order-created'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name = "order-detail"),
    path('my_orders/<int:pk>/', views.UserOrderListView.as_view(), name = "my-orders")
]