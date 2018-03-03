from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
	all_questions = Question.objects.all()
	response = ', '.join([q.question_text for q in all_questions])
	return HttpResponse(response)
