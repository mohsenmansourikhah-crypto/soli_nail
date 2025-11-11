from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Gallery

# Create your views here.

class GalleryView(ListView):
    model = Gallery
    template_name = "gallery_module/gallery_page.html"
    context_object_name = "galleries"
    paginate_by = 5

