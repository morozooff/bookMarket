from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list = ("name", "biography", "avatar")


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "pages_num", "author", "cost", "review", "cover")
    list_filter = ("author", )

