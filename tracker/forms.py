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


class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['editor', 'author_profile', 'user', 'likes', 'comment',]


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'django_registration/edit_profile.html'
    success_url = reverse_lazy('index')

class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = Profile
        fields = ['first_name', 'email', 'first_name', 'last_name', 'bio', 'phone_number',]
        widgets = {
            # 'user': models.OneToOneField(User, on_delete=models.CASCADE),
            'bio': forms.Textarea(attrs={'rows': 3}),
            'first_name': forms.TextInput(attrs={'rows': 1}),
            'email': forms.TextInput(attrs={'rows': 1}),
            'phone_number': forms.NumberInput(attrs={'rows': 1}),
            'location': forms.TextInput(attrs={'rows': 1}),
        }