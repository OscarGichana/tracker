from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth import views 
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Neighborhood,Profile,Posts,Business
from django.http  import HttpResponse,Http404
from .forms import ProfileUpdateForm,NewProjectForm,NewNeighborhoodForm,UserUpdateForm
from django.views import generic
from django.urls import reverse_lazy
from django.template import RequestContext
# from django.core import urlresolvers

# Create your views here.
def index(request):
    date = dt.date.today()
    neighborhoods = Neighborhood.get_neighborhoods()
    title = 'O_world'

    # if 'neighborhood' in request.GET and request.GET["neighborhood"]:
    #     neighborhoods = request.GET.get("neighborhood")
    #     # searched_neighborhood = Business.get_by_neighborhood(neighborhoods)
    #     all_posts = Posts.get_by_neighborhood(neighborhoods)
    #     message = f"{neighborhoods}"
    #     all_neighborhoods = Neighborhood.get_neighborhoods()        
        

    # else:
    #     message = "No Neighborhood Found!"

    return render(request, 'index.html', {'neighborhoods': neighborhoods}, )

def neighborhood(request, neighborhood_id):
    title = 'neighborhood'
    try:
        neighborhood = Neighborhood.objects.get(id = neighborhood_id)
        posts = Posts.get_posts(Posts, id= neighborhood_id)
        business = Business.get_business(Business, id= neighborhood_id)

    except Neighborhood.DoesNotExist:
        raise Http404()

    # if 'neighborhood' in request.GET and request.GET["neighborhood"]:
    #     neighborhoods = request.GET.get("neighborhood")
    #     # searched_neighborhood = Business.get_by_neighborhood(neighborhoods)
        # posts = Posts.get_by_neighborhood(neighborhoods)
    #     message = f"{neighborhoods}"
    #     all_neighborhoods = Neighborhood.get_neighborhoods()        
        

    # else:
    #     message = "No Neighborhood Found!"

    return render(request, 'posts.html', {'neighborhood':neighborhood,'business':business,'posts':posts,'id':neighborhood_id, 'title':title})

# @login_required(login_url='/accounts/login/')
# def posts(request, id):
#     title = 'O_world'
#     posts = Posts.get_by_neighborhood(neighborhoods)
#     message = f"{neighborhoods}"
#     return render(request, 'posts.html', {'posts':posts, 'title':title, 'message':message})



class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'django_registration/registration_form.html'
    success_url = reverse_lazy('login')

# class UserEditView(generic.UpdateView):
#     form_class = UserChangeForm
#     template_name = 'django_registration/edit_profile.html'
#     success_url = reverse_lazy('index')
    
#     def get_object(self):
#         return self.request.user

# @login_required 
# def edit_profile( request, template_name = 'django_registration/edit_profile.html' ):
#     """
#     Processes requests for the settings page, where users
#     can edit their profiles.
#     """
#     page_title = 'Account Settings'
#     if request.method == 'POST':
#         postdata = request.POST.copy()
#         form = UserUpdateForm( postdata )
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserUpdateForm()
#     title = 'Settings'
#     return render(request, 'django_registration/edit_profile.html', )


@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'O_world'
    user = request.user
    return render(request, 'django_registration/profile.html')


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('index')

    else:
        form = UserUpdateForm()
    return render(request, 'django_registration/edit_profile.html', {"form": form})
    def get_object(self):
        return self.request.user



@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_neighborhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.editor = current_user
            neighborhood.save()
        return redirect('index')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'new_neighborhood.html', {"form": form})


def search_neighborhoods(request):

    # search for a user by their username
    if 'neighborhood' in request.GET and request.GET["neighborhood"]:
        search_term = request.GET.get("project")
        searched_neighborhoods = Neighborhood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "neighborhood": searched_neighborhoods})

    else:
        message = "You haven't searched for any neighborhood"
        return render(request, 'search.html', {"message": message})
