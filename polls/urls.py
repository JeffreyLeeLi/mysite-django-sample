from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
	# /polls/
	path('', views.index, name='index'),

	# /polls/1/
	path('<int:question_id>/', views.detail, name = 'detail')
]