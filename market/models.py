from django.db import models
from PIL import Image as Im # new
from django.urls import reverse

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