from django.urls import path
from . import views

urlpatterns = [
    #set end points and pass in getData view
    path('', views.getData),
    path('add/', views.addItem)
]