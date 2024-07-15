from django.db import models
from django.urls import reverse


class ContactMessage(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Name')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    subject = models.CharField(max_length=100, blank=True, verbose_name='Subject')
    message = models.TextField(max_length=500, blank=False, null=False, verbose_name='Message')
    datetime_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

