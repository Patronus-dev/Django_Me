from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', my_view, name='home'),
    path('contact/', ContactCreateView, name='contact'),

]
