from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.



@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("login", "email", "orders")
    exclude = ["password", ]


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list = ("name", "biography")


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "pages_num", "author", "cost", "review")
    list_filter = ("author", )

class BookInline(admin.TabularInline):
    model = Order.books.through

@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", )
    exclude = ["books", ]
    list_filter = ("status",)
    inlines = [
        BookInline,
    ]