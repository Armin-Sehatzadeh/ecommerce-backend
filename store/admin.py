from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "stock"]
    search_fields = ["name"]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)