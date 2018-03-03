from django.urls import path

from . import views
from .apps import PollsConfig

app_name = PollsConfig.name

urlpatterns = [
	# /polls/
	path('', views.index, name = 'index'),

	# /polls/1/
	path('<int:question_id>/', views.detail, name = 'detail')
]