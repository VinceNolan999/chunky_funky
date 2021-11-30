'''
creates the Url for the profile view
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile')
]
