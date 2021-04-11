from django.shortcuts import render
from django.contrib.auth import views 
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    # projects = Project.get_all_projects()
    # locations = Location.objects.all()
    title = 'O_world'
    return render(request, 'index.html', )



class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'django_registration/registration_form.html'
    success_url = reverse_lazy('login')