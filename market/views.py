from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
