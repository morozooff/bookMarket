from datetime import datetime

from django.db import models
from market.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, default = 'Moscow')
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(default=datetime.now())
    ORDER_STATUS = (
        ('S', 'Формируется'),
        ('NP', 'Не оплачен'),
        ('C', 'Собран'),
        ('ID', 'В доставке'),
        ('D', 'Доставлен'),
        ('ND', 'Недоставлен')
    )
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default = 'S')

    def status_verbose(self):
        return dict(Order.ORDER_STATUS)[self.status]

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name = 'order_items', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.cost * self.quantity