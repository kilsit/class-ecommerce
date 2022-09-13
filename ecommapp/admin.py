from django.contrib import admin
from .models import *

# admin.site.register([Category, Product, Cart, CartProduct, Order, ProductImage])
admin.site.register([Customer, Category, Product, Cart, CartProduct, Order, ProductImage])
