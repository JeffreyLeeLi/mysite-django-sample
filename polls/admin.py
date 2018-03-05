from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	list_filter = ['pub_date']
	list_display = ['question_text', 'pub_date', 'was_published_recently']

	fieldsets = [
		(None, {
			'fields': ['question_text'],
		}),

		('Date Information', {
			'fields': ['pub_date'],
			'classes': ['collapse'],
		}),
	]

	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
