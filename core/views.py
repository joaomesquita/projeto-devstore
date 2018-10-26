from django.shortcuts import render
from django.views import generic

from catalog.models import Product

# Create your views here.
class IndexView(generic.ListView):

    model = Product
    template_name = 'index.html'

index = IndexView.as_view()
