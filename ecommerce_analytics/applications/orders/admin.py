from django.contrib import admin
from .models import Orders, OrderItems, OrderItemRefunds

# Register your models here.

admin.site.register([Orders, OrderItems, OrderItemRefunds])