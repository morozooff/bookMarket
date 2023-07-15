from django.db import models

# Create your models here

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    pages_num = models.IntegerField()
    cost = models.IntegerField()
    review = models.TextField()
    # avatar = models.FileField()

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


class User(models.Model):
    login = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    orders = models.ForeignKey(Order, on_delete= models.CASCADE)
    # avatar = models.FileField()
