from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blockchain'

urlpatterns = [
    path('success', views.success, name='succeded'),
    path('check_integrity', views.check_integrity, name='check_integrity'),

]
