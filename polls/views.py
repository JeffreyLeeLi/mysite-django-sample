from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
	all_questions = Question.objects.all()
	template = loader.get_template('polls/index.html')

	context = {
		'all_questions': all_questions,
	}

	response = template.render(context, request)

	return HttpResponse(response)

def detail(request, question_id):
	return HttpResponse("Question: %s" % question_id)
