from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# path takes 4 arguments; 2 required and 2 optional
#   route - string that contains URL pattern
#   view
#   kwargs
#   name - lets you refer to URL unambiguously within templates