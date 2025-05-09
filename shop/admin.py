from django.contrib import admin # type: ignore
from .models import Product, Category, Tag, Order, OrderItem

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(OrderItem)
