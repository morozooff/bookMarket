from rest_framework.serializers import ModelSerializer
from .models import *


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'cost', 'cover']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'status']