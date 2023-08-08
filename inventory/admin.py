from django.contrib import admin

from .models import Category, Inventory


admin.site.register(Category)
admin.site.register(Inventory)