from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from site_module.models import Slider, Popular, Product
from django.core.paginator import Paginator


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['slider'] = sliders
        return context


class PopularListView(ListView):
    model = Popular
    template_name = "home_module/popular_page.html"
    context_object_name = "popular"
    paginate_by = 8

# class PopularDetailView(DetailView):
#     model = Popular
#     template_name = "home_module/popular_page.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return render(self.request, "home_module/popular_detail_page.html", context)
def popular_detail(request, popular_id):
    try:
        images = Popular.objects.get(id=popular_id)
    except:
        raise Http404

    return render(request, "home_module/popular_detail_page.html", {
        "images": images
    })



class ProductListView(ListView):
    model = Product
    template_name = "home_module/product_list.html"
    context_object_name = "product"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     populars = Popular.objects.all()
    #     context['popular'] = populars
    #     return context

    # def get_queryset(self):
    #     return Popular.objects.filter(is_active=True)

    # def popular_page(request):


#     populars = Popular.objects.all()
#     context = {
#         "popular": populars
#     }
#     return render(request, "home_module/popular_page.html", context)
def product_detail(request, product_id):
    try:
        products = Product.objects.get(id=product_id)
    except:
        raise Http404

    return render(request, "home_module/product_detial_page.html", {
        "product": products
    })


class HeaderComponent(TemplateView):
    template_name = 'shared/header_component.html'


class FooterComponent(TemplateView):
    template_name = "shared/footer_component.html"
