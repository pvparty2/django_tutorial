from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice

# Create your views here.
def index(request):
    # create list of first 5 questions ordered by decreasing publication date
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    context = {'latest_question_list': latest_question_list}
    # when /polls/ is accessed return index.html
    # index.html uses the variables in dictionary (third optional argument)
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Code below does the same as one liner above.
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = f'You\'re looking at results of question {question_id}.'
    return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))