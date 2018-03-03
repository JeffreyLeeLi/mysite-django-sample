from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'

	context_object_name = 'question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
	model = Question
	template_name = 'polls/result.html'

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
