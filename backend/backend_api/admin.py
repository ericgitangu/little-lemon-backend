from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'status']
    list_per_page = 20


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ['order__user__username', 'menu_item__name']
    list_per_page = 15


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category__name']
    list_per_page = 25
