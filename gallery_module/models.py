from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان عکس")
    image = models.ImageField(upload_to="uploads/gallery/", verbose_name="تصویر")
    is_delete = models.BooleanField(verbose_name="حذف شده / نشده")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "تصویر گالری"
