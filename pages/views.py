from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext

from django.views.generic import *
from .forms import ContactMessageForm
from blog.models import Blog


class HomePageView(TemplateView):
    template_name = 'home.html'

    #  in this part , we can access to Values of app.models on home page
    def get_context_data(self, **kwargs):
        #  in this part , we can access to all blogs by id
        context = super().get_context_data(**kwargs)
        context['all_blogs'] = Blog.objects.all().order_by('-id')
        #  in this part , we can access to 3 latest post in blogs by id
        latest_blogs = Blog.objects.all().order_by('-id')[:3][::-1]
        context['latest_blogs'] = latest_blogs
        return context


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
    return render(request, 'home.html', {'form': form})


def my_view(request):
    return render(request, '_base.html')
