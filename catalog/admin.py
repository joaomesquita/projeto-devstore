from django.contrib import admin
from .models import Product, Category, Size, ProductVariation, ProductImage

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']

class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1

class ProductImagemInline(admin.TabularInline):
    model = ProductImage
    extra = 4

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
    inlines = [ProductVariationInline, ProductImagemInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
