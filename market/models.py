from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image as Im # new
from django.contrib.auth.models import User
from django.urls import reverse
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
    tags = models.TextField(default = 'Book')
    cover = models.ImageField(upload_to = 'images', blank = True, null = True)

    def save(self):
        super().save()
        image = Im.open(self.cover.path)
        if image.height > 300 or image.width > 300:
            correct_params = (300, 300)
            image.thumbnail(correct_params)
            image.save(self.cover.path)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})


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
