from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')
    

class User(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email =models.CharField(max_length=200,null=True)
    profile= models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name






class NeighbourHood(models.Model):
     Name = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     population = models.IntegerField()
     image = models.ImageField(blank=True,null=True)
     healthno = models.IntegerField(null=True)
     policeno = models.IntegerField(null=True)

     def __str__(self):
         return self.Name


class Business(models.Model):
    businessname = models.CharField(max_length=255)
    email =models.EmailField(max_length=100)
    image = models.ImageField(blank=True,null=True)
    created_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.businessname

    @classmethod
    def search_category(cls,search):
        searches = cls.objects.filter(businessname__icontains = search)
        return searches
    



        
