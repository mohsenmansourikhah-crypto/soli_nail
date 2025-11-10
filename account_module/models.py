from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(blank=True, db_index=True, verbose_name="تصویر اواتار")
    email_active_code = models.CharField(max_length=200, verbose_name='کد فعال سازی ایمیل')

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرات'