from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('',views.index, name="index"), 
    path('about/',views.about, name="about"), 
    path('menu/',views.menu, name="menu"),
    path('contact/',views.contact, name="contact"), 
    path('coffee-blend-drinks/',views.drinks, name="drinks"), 
    path('coffee-blend-food/',views.food, name="food"), 
    path('cart/',views.Cart, name="cart"), 
    path('checkout/',views.checkout, name="checkout"), 
    path('update_cart/',views.updateCart, name="updateItem"), 
    path('process_order/',views.ProcessOrder, name="processOrder"), 
    path('register/',views.Registration, name="registration"), 
    path('login/',views.Login, name="login"), 
    path('logout/',views.LogoutUser, name="logout"), 
]