from django.contrib import admin
from django.urls import path
from newsapp import views
app_name='newsapp'

urlpatterns = [
   path('',views.index,name='index'),
   path('international/',views.international,name='international'),
   path('tech/',views.tech,name='tech'),
   ]
