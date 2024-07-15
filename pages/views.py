from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from django.views.generic import *
from .forms import ContactMessageForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


def ContactCreateView(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            send_mail(
                'New Contact Message',
                f'Message from {contact_message.name} ({contact_message.email}):\n\n{contact_message.message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = ContactMessageForm()
    return render(request, 'pages/home.html', {'form': form})
