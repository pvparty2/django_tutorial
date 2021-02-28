from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# path takes 4 arguments; 2 required and 2 optional
#   route - string that contains URL pattern
#   view
#   kwargs
#   name - lets you refer to URL unambiguously within templates