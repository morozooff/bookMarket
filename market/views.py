from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from .logic.validations import *



def catalog(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'market/catalog.html', context)

def about(request):
    return render(request, 'market/about.html', {'title': 'О магазине TolStore'})


def home(request):
    return render(request, 'market/home.html')

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


