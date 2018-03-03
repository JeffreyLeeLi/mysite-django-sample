from django.urls import path

from . import views
from .apps import PollsConfig

app_name = PollsConfig.name

urlpatterns = [
	# /polls/
	path('', views.index, name = 'index'),

	# /polls/1/
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),

	# /polls/1/result/
	path('<int:question_id>/result', views.result, name = 'result'),

	# /polls/1/vote/
	path('<int:question_id>/vote', views.vote, name = 'vote'),
]