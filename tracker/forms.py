from django import forms
from .models import *
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['editor', 'author_profile', 'user', 'likes', 'comment',]



class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['editor', 'author_profile', 'user', 'likes', 'comment',]


