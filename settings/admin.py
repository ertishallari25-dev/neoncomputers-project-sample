from django.contrib import admin
from .models import Product, ContactMessage, Order 

admin.site.register(Product)
admin.site.register(ContactMessage)
admin.site.register(Order)