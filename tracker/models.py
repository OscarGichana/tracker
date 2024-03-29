from __future__ import unicode_literals
from django.db import models
import datetime as dt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db.models.signals import (post_save,pre_save,)
# from PIL import Image
from django.core.files import File
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Avg, Max, Min
from django_countries.fields import CountryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 60,null=True,blank=True)
    last_name = models.CharField(max_length = 60,null=True,blank=True)
    pic = CloudinaryField('pic',null=True) 
    bio = models.TextField(null=True,blank=True)
    likes = models.IntegerField(default=0)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=True)
    location = models.CharField(max_length = 60,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)
    def create_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


    def get_total_likes(self):
        return self.likes.user.count()


def create_profile(sender, instance, created, **kwargs):
    if created: Profile.objects.create(user=instance)

post_save.connect(create_profile, sender = User)



class Neighborhood(models.Model):
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length = 60,null=True,blank=True)
    location = models.CharField(max_length = 60,null=True,blank=True)
    count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    country = CountryField(blank_label='(select country)', default='KE')
    health = models.CharField(max_length = 60,null=True,blank=True)
    police = models.CharField(max_length = 60,null=True,blank=True)
    fire = models.CharField(max_length = 60,null=True,blank=True)
    pic = CloudinaryField('pic',null=True) 

    def __str__(self):
        return str(self.user.username)
    class Meta:
        ordering = ['name']
    def create_neighborhood(self):
        self.save()
    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def get_neighborhoods(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_by_title(cls,search_term):
        neighborhood = cls.objects.filter(title__icontains=search_term)
        return neighborhood

    
    
    @classmethod
    def get_by_admin(cls, Admin):
        projects = cls.objects.filter(Admin=Admin)
        return projects
    
    
    @classmethod
    def get_neighborhood(request, neighborhood):
        try:
            project = Neighborhood.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Neighborhood'

        verbose_name_plural = 'Neighborhoods'


class Posts(models.Model):
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)    
    Author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE, related_name="neighborhood")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')


    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()
        

    def get_posts(self, id):
        posts = Posts.objects.filter(neighborhood_id =id)
        return posts

    @classmethod
    def get_allpost(cls):
        posts = cls.objects.all()
        return posts
    
    @classmethod
    def get_by_neighborhood(cls, neighborhoods):
        posts = cls.objects.filter(neighborhood__name__icontains=neighborhoods)
        return posts
    
    def __str__(self):
        return self.post
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Post'
        verbose_name_plural = 'Posts'


class Business(models.Model):
    name = models.TextField()
    email = models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)    
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True, on_delete=models.CASCADE, related_name="bus_neighborhood")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='bus_user')


    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
        

    def get_business(self, id):
        business = Business.objects.filter(neighborhood_id =id)
        return business

    def update_business(self, id):
        business = Business.objects.filter(business_name =name)
        return business
