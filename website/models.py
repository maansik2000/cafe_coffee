from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE , blank=True)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.fname
    
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    subject = models.CharField(max_length = 122)
    desc = models.TextField()
    
    def __str__(self):
        return self.subject


class QuerySection(models.Model):
    FirstName = models.CharField(max_length = 122)
    LastName = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122,null=True)
    phone = models.CharField(max_length = 122,null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.desc

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    Description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    dateTime =  models.DateTimeField(auto_now=False, auto_now_add=False, blank = True, null=True)
    
    def __str__(self):
        return str(self.id)
    
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_discount(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        discount = (total*10)/100
        return discount
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        discount = total - self.get_discount
        return discount
    

        
        
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True) #child of order  
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class pickupTime(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=200, null=True)
    zipCode = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.time