from django.shortcuts import render
from django.http import Http404

from .models import Question

# Create your views here.

def index(request):
	all_questions = Question.objects.all()
	context = {
		'all_questions': all_questions,
	}

	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		q = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")

	context = {
		'question': q,
	}

	return render(request, 'polls/detail.html', context)
