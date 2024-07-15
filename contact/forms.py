from django import forms
from .models import ContactUs


class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'subject', 'email', 'message']
