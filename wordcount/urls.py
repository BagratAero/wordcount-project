

from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('aboutus/', views.aboutpage, name='about')
    #name is connected to name in home.html line 4, independent of the path "count/" .. so you can chang the name of the url, and it will all still work
]
