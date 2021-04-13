from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import UserRegisterView


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^profile',views.profile,name = 'profile'),
    url(r'^neighborhood/(\d+)',views.neighborhood, name='neighborhood'),
    url(r'^edit_profile',views.edit_profile,name = 'edit-profile'),
    url(r'^new/neighborhood$', views.new_neighborhood, name='new-neighborhood'),
    url(r'^new/post$', views.new_project, name='new-project'),
    url(r'registration/', UserRegisterView.as_view(), name='registration'),
    url(r'^search/', views.search_neighborhoods, name='search_neighborhoods'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
