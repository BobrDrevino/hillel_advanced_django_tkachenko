from django.contrib import admin
from orders.models import Order, Discount


@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    # list_display = ('name', 'created_at')
    list_filter = ('created_at',)


@admin.register(Discount)
class ItemAdmin(admin.ModelAdmin):
    # list_display = ('name', 'created_at')
    list_filter = ('created_at',)