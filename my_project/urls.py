"""
URL configuration for my_project 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #connect root urls to urls in API folder
    path('', include('api.urls')),
]
