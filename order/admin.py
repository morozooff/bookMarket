from django.contrib import admin
from .models import *
from django.contrib.admin.decorators import register
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']

@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "address", "postal_code", "created", "status" ]
    list_filter = ("status",)
    inlines = [
        OrderItemInline,
    ]
