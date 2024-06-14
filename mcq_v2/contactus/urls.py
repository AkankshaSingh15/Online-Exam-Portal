from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import contactushere

urlpatterns = [
    path('',contactushere, name = 'contact'),
    
    ]
