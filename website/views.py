from django.shortcuts import render, HttpResponse
from website.models import Contact, AskIndex, Product
from django.contrib import messages
from .models import *

# Create your views here.
#url dispatching
def index(request):   
    
    foodItem = Product.objects.all()[:4]
    
    context = {'product':foodItem}
    
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        askIndex = AskIndex(FirstName = FirstName,LastName = LastName, email = email, phone = phone, desc = desc)
        askIndex.save()
        messages.success(request,"We will get back to you as soon as possible")

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def menu(request):
    foodItem = Product.objects.all()[:26]
    dessert = Product.objects.all()[40:50]
    context = {'product':foodItem,"dessert":dessert}
    return render(request,'menu.html',context)


def drinks(request):
    drinks = Product.objects.all()

    context = {'product' : drinks}
    
    return render(request,'drinks.html', context)


def food(request):
    drinks = Product.objects.all()
    context = {'product' : drinks}
    return render(request,'food.html',context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        print(name)
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, subject = subject, desc = desc)
        contact.save()
        messages.success(request,"your message has been sent")
    return render(request,'contact.html')
    
