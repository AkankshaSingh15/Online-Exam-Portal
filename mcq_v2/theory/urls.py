from django.urls import path
#from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from theory.models import Quest
from . import views
from theory.views import *
#from theory.views import details
import re
from django.db import models
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = [
    path('',views.index),
    path('ctutorial/',views.ctutorial, name='ctutorial'),
    path('cplus/',views.cplus, name='cplus'),
    path('java/',views.java, name='java'),
    path('python/',views.python, name='python'),
    path('aptitude/',views.aptitude, name='aptitude'),
    path('hc/',views.hc,name='hc'),
    ]
    
