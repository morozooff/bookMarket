from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list = ("name", "biography")


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "pages_num", "author", "cost", "review", "cover")
    list_filter = ("author", )


class BookInline(admin.TabularInline):
    model = Order.books.through

@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", )
    exclude = ["books", "users"]
    list_filter = ("status",)
    inlines = [
        BookInline,
    ]
