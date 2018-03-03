from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

def index(request):
	all_questions = Question.objects.order_by('-pub_date')
	context = {
		'all_questions': all_questions,
	}

	return render(request, 'polls/index.html', context)

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

def result(request, question_id):
	q = get_object_or_404(Question, pk = question_id)
	context = {
		'question': q,
	}

	return render(request, 'polls/result.html', context)

def vote(request, question_id):
	q = get_object_or_404(Question, pk = question_id)

	try:
		s = q.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		context = {
			'question': q,
			'error_message': 'Invalid choice',
		}

		print('exception occurred')

		return render(request, 'polls/detail.html', context)
	else:
		s.votes += 1
		s.save()

		return HttpResponseRedirect(reverse('polls:result', args = (q.id,)))
