from django.shortcuts import render
from django.http import HttpResponse


from .models import Question

# Create your views here.
def index(request):
    # create list of first 5 questions ordered by decreasing publication date
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    context = {'latest_question_list': latest_question_list}
    # when /polls/ is accessed return index.html
    # index.html uses the variables in dictionary (third optional argument)
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}.')

def results(request, question_id):
    response = f'You\'re looking at results of question {question_id}.'
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}.')