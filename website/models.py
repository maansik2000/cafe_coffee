from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    subject = models.CharField(max_length = 122)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class AskIndex(models.Model):
    FirstName = models.CharField(max_length = 122)
    LastName = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122,null=True)
    phone = models.IntegerField(null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.FirstName
    
    
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