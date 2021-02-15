from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name = 'profile'),
    path('aboutus', views.aboutus, name = 'aboutus'),
    
    url(r'^signup/$', views.signup, name='signup'),
   
]
