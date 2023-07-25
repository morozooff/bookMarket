from django.contrib import admin
from .models import *
from django.contrib.admin.decorators import register
# Register your models here.

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