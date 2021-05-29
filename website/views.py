from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
#url dispatching
def index(request):   
    
    if request.user.is_authenticated:
        u = request.user
        print(u)
        customer1,created = Customer.objects.get_or_create(
            user = u
        )
        customer1.save()
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items
       # print(items[1].product.name)  
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    foodItem = Product.objects.all()[:4]
    
    context = {'product':foodItem,'cartItems':cartItems}
    
    if request.method == "POST":
        Fname = request.POST.get('FirstName')
        Lname = request.POST.get('LastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        query_section = QuerySection(FirstName = Fname, LastName = Lname,email=email, desc= desc, phone=phone )
        query_section.save()
        messages.success(request,"We will get back to you as soon as possible")

    return render(request,'index.html',context)

def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items
       # print(items[1].product.name)  
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    context = {'cartItems':cartItems}
    
    return render(request,'about.html',context)

def menu(request):
    dessert = Product.objects.all()[40:50]
    foodItem = Product.objects.all()[:26]
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
            #get all the order items
       # print(items[1].product.name)  
        cartItems = order.get_cart_items
    else:
        
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    context = {'product':foodItem,'cartItems':cartItems,"dessert":dessert}

    return render(request,'menu.html',context)


def drinks(request):
    drinks = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items
       # print(items[1].product.name)  
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    context = {'product':drinks,'cartItems':cartItems}
    return render(request,'drinks.html', context)

def food(request):
    drinks = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items
       # print(items[1].product.name)  
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    context = {'product':drinks,'cartItems':cartItems}
    return render(request,'food.html',context)


def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items
       # print(items[1].product.name)  
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
     
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        print(name)
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, subject = subject, desc = desc)
        contact.save()
        messages.success(request,"your message has been sent")
    
    context = {'cartItems':cartItems}   
    return render(request,'contact.html',context)
    
@login_required(login_url='login')
def Cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items

        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    context = {'items' : items,'order':order,'cartItems':cartItems}
    return render(request,'cart.html',context)

@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer

        order, created = Order.objects.get_or_create(customer = customer,complete = False)
        items = order.orderitem_set.all()    #get all the order items

        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'get_discount' : 0,'get_total' :0}
        cartItems = order['get_cart_items']
    
    context = {'items' : items,'order':order,'cartItems':cartItems}
    return render(request,'checkout.html',context)


def updateCart(request):
    
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('productId:',productId)
    print('action:',action)
    
    customer = request.user.customer
    foodItem = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer,complete = False)
    
    
    orderItem, created = OrderItem.objects.get_or_create(order = order, product=foodItem)
    
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == "delete":
        orderItem.quantity = 0
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added ', safe=False)


def ProcessOrder(request):
    print('data',request.body)
    data = json.loads(request.body)
    dateTime = datetime.datetime.now()
    transaction_id = datetime.datetime.now().timestamp()
    
    if request.user.is_authenticated:
        customer = request.user.customer
        customer.fname = data['form']['fname']
        customer.lname = data['form']['lname']
        customer.phone = data['form']['phone']
        customer.email = data['form']['email']
        customer.save()
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        total = float(data['form']['total'])
        
        if total == order.get_total:
            order.complete = True
            order.transaction_id = transaction_id
            order.dateTime = dateTime
        order.save()
        
        pickupTime.objects.create(
            customer = customer,
            order = order,
            state = data['form']['select_state'],
            zipCode = data['form']['zipCode'],
            time = data['form']['timePicker']
        )

    else:
        print('user is not logged in')
    
    return JsonResponse('Payment complete', safe=False)



def Registration(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        form = CreateUserForms()
        
        if request.method == 'POST':
            form = CreateUserForms(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Your account has created " + user)
                return redirect('login')

    context = {'form' : form}
    return render(request,'register.html',context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,"Username or password is incorrect")
        
    return render(request,'login.html')



def LogoutUser(request):
    logout(request)
    return redirect('login')
