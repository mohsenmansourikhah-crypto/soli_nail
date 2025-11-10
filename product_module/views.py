from django.shortcuts import render
from site_module.models import Product
from django.views.generic.list import ListView


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "product_module/product_list2.html"
    context_object_name = "product2"