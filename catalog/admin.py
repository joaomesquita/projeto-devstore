from django.contrib import admin

from .models import Product, Category, Size, ProductVariation

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']

#class ImageAdmin(admin.ModelAdmin):
#    list_display = ['image']
#    search_fields = ['image']

class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1

#class ProductImageInline(admin.TabularInline):
#    model = ProductImage
#    extra = 4

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
    inlines = [ProductVariationInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
#admin.site.register(Image, ImageAdmin)
