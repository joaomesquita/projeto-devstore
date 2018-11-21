from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django_object_actions import DjangoObjectActions
from weasyprint import HTML

from .models import CartItem, Order, OrderItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity']
    search_fields = ['product__name']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
    search_fields = ['order','product__name']

class OrderAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['__str__', 'user', 'status', 'created', 'modified']
    search_fields = ['user__name']
    list_filter = ['created', 'modified']

    def generate_pdf(self, request, obj):
        html_string = render_to_string('reports/pdf_order.html', {'obj': obj})
        html = HTML(string=html_string)
        html.write_pdf(target='reports/checkout/{}.pdf'.format(obj));
        fs = FileSystemStorage('reports/checkout')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response
        return response

    generate_pdf.label = 'Gerar PDF'
    generate_pdf.short_description = 'Clique para gerar o PDF do pedido'
    change_actions = ('generate_pdf',)

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
