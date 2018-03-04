import datetime

from django.utils import timezone
from django.urls import reverse
from django.test import TestCase, Client

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days = 30)
		future_question = Question(pub_date = time)

		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
		future_question = Question(pub_date = time)

		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
		future_question = Question(pub_date = time)

		self.assertIs(future_question.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):
	client = Client()

	def test_no_questions(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls available")
		self.assertQuerysetEqual(response.context['question_list'], [])