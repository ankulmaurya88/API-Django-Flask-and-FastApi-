from django.urls import path 
from . import views



app_name = 'scaper'

urlpatterns=[
    path('',views.home,name='hmoe'),
]