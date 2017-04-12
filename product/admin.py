from django.contrib import admin
from .models import *


class ProductAdminInline(admin.TabularInline):
    model = Product
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    inlines = [ProductAdminInline]

    class Meta:
        model = Category


class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
