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

    def get_total_likes(self):
        return self.likes.user.count()

    @classmethod
    def update_profile(cls, id, email, phone_number, first_name, last_name, bio, pic):
        profile = cls.objects.filter(id = id).update(pic = pic, id = id, first_name=first_name, last_name=last_name,bio=bio,phone_number=phone_number, email=email)
        
        return update


    def __str__(self):
        return str(self.user.username)
    class Meta:
        ordering = ['first_name']
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


def create_profile(sender, instance, created, **kwargs):
    if created: Profile.objects.create(user=instance)

post_save.connect(create_profile, sender = User)
