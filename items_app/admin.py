from django.contrib import admin
from .models import ProductType, ProductItems
# Register your models here.

admin.site.register(ProductType)
admin.site.register(ProductItems)