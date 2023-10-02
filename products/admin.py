from django.contrib import admin
from .models import Product,Category,Subcategory


admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Subcategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
