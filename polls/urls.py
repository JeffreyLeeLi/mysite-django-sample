from django.urls import path

from . import views
from .apps import PollsConfig

app_name = PollsConfig.name

urlpatterns = [
	# /polls/
	path('', views.IndexView.as_view(), name = 'index'),

	# /polls/1/
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),

	# /polls/1/result/
	path('<int:pk>/result', views.ResultView.as_view(), name = 'result'),

	# /polls/1/vote/
	path('<int:question_id>/vote', views.vote, name = 'vote'),
]