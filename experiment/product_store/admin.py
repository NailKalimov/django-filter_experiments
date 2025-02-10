from django.contrib import admin

from .models import Product, Manufacturer


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' ,'price', 'description', 'release_date')

@admin.register(Manufacturer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )