from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

# Create your views here.
def contactushere(request):
        
    if request.method=='POST':
       nm=request.POST.get('name')
       eml=request.POST.get('email')
       msg=request.POST.get('msg')
       ph=request.POST.get('pnumber')
       print(nm,eml,ph,msg)
       user=Contact(name =nm,email =eml,pnumber =ph,msg =msg)
       user.save()
       messages.success(request, "your message send sucessfully .")
        
    return render(request,'contactus/contact.html')
    

    

                
            
        
        
    
