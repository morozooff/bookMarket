from django.db import models
from market.models import Book
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    order_id = models.CharField(max_length=255, primary_key=True)
    books = models.ManyToManyField(Book)
    ORDER_STATUS = [
        ('S', 'Started'),
        ('NP', 'Not paid'),
        ('C', 'Construct'),
        ('ID', 'In Delivery'),
        ('D', 'Delivered'),
        ('ND', 'Not Delivered')
    ]
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default = 'S')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
