from select import select
from tkinter.tix import Select
from unittest import result

from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.contrib import messages
from requests import Response, request
from home.models import Contact
from home.models import services

# Create your views here.
def index(request):
    
    return render(request,"index.html")
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is about page")

def Services(request):
    if request.method =="POST":
      Select=request.POST.get("Select")
      name=request.session.get("name")
      ayush=services.objects.create(Select=Select,name=name)
      return render(request,"services.html")

    else:
        return render(request,"services.html")

    #return HttpResponse("this is services page")

def contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        request.session["name"]=name
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return render(request,"contact.html")
    else:
        return render(request,"contact.html")
        
    #return HttpResponse("this is contact page")
    #making queries django
    #__startswith
