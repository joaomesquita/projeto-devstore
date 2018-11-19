from django.contrib import admin
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from django.template.loader import render_to_string

# from weasyprint import HTML
from django_object_actions import DjangoObjectActions

from .models import CartItem, Order, OrderItem

# Register your models here.
class CartItemAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity']
    search_fields = ['product__name']

    def test(self, request, obj):
        print('test')

    test.label = 'Gerar PDF'
    test.short_description = 'Clique para gerar o PDF dessa ordem de serviço'
    change_actions = ('test',)

    # def generate_pdf(self, request, obj):
    #     html_string = render_to_string('reports/pdf_template.html', {'obj': obj})

    #     html = HTML(string=html_string)
    #     html.write_pdf(target='/tmp/{}.pdf'.format(obj))

    #     fs = FileSystemStorage('/tmp')
    #     with fs.open('{}.pdf'.format(obj)) as pdf:
    #         response = HttpResponse(pdf, content_type='application/pdf')
    #         response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
    #         return response
    #     return response

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
    search_fields = ['order','product__name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'status', 'created', 'modified']
    search_fields = ['user__name']
    list_filter = ['created', 'modified']

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
