from django.urls import path
from . import views

purlatterns = [
    path(".",views.home,"Show"),
    path('Delete',views.delete,"Delete"),
    path("Update",views.update,"Update"),
    path("Write",views.write,"Write")
]