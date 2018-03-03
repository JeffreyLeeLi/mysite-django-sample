from django.shortcuts import render, get_object_or_404
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
	q = get_object_or_404(Question, pk = question_id)
	context = {
		'question': q,
	}

	return render(request, 'polls/detail.html', context)
