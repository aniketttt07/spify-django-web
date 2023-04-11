from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),      # Also use this -->  path('', views.index, name='home'),
    path('article', views.article, name='article'), 
    path('terms', views.terms, name='terms'), 
    path('privacy', views.privacy, name='privacy'), 

]
