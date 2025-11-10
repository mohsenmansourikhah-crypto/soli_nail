from django.db import models
from django.urls import reverse


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان اسلایدر')
    images = models.ImageField(upload_to='uploads/slider', verbose_name='تصویر اسلایدر')
    url = models.CharField(max_length=200, verbose_name="لینک")
    url_title = models.CharField(max_length=200, verbose_name="عنوان لینک")
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیز فعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدرها"


class Popular(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    images = models.ImageField(upload_to='uploads/popular', verbose_name="تصویر بازدید")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیر فعال")

    def get_absolute_url(self):
        return reverse("popular-detail", args=[self.id])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تصویر پر بازدید"
        verbose_name_plural = "پر بازدیدها"


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    images = models.ImageField(upload_to="uploads/product", verbose_name="تصویر محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیر فعال")

    def get_absolute_url2(self):
        return reverse("product-detail", args=[self.id])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
