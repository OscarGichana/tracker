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

