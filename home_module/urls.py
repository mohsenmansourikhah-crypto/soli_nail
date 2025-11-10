from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home-page'),

    path("<int:popular_id>", views.popular_detail, name="popular-detail"),
    path("<int:product_id>", views.product_detail, name="product-detail"),

]