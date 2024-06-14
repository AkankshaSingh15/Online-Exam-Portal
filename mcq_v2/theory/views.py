from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import *
from theory.models import Quest
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url="/login/")
def index(request):
    context = {}
    questions= Quest.objects.all()#query sent to the database
    context['title'] = 'Subjective Queries'
    context['questions'] = questions
    return render(request,"theory/theory.html",context)

'''def details(request,id):
    context = {}
    question = Quest.objects.get()
    description = Answer.objects.all()
    #choice = Choice.objects.all)
    context['question'] = question
    context['description'] = description
    return render(request, 'theory/one.html',context)'''

def aptitude(request):
    return render(request,"theory/aptitude.html")

def cplus(request):
    return render(request,"theory/cplus.html")

def ctutorial(request):
    return render(request,"theory/ctutorial.html")

def java(request):
    return render(request,"theory/java.html")

def python(request):
    return render(request,"theory/python.html")

def hc(request):
    return render(request,"theory/hc.html")




