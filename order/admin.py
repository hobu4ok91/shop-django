from django.contrib import admin
from .models import *


class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Order._meta.fields]
    inlines = [OrderProductsInline]

    class Meta:
        model = Order


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OrderStatus._meta.fields]

    class Meta:
        model = OrderStatus


class OrderProductsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in OrderProducts._meta.fields]

    class Meta:
        model = OrderProducts


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProducts, OrderProductsAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
