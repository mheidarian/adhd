from django.db import models
from django.utils import timezone

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=255, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ارسال")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
