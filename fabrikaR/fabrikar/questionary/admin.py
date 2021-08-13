from django.contrib import admin

from .models import Questionary, Question, Answer, TestQuest


class QuestionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_at', 'end_date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'quest_text', 'questionary')
    list_display_links = ('id', 'quest_text')
    search_fields = ('id', 'quest_text')
    list_filter = ('questionary',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer_text', 'question')
    list_display_links = ('id', 'answer_text')
    search_fields = ('id', 'answer_text')

class TestQuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'questionary', 'question', 'answer')
    list_display_links = ('id',)
    search_fields = ('id', 'questionary')

admin.site.register(Questionary, QuestionaryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(TestQuest, TestQuestAdmin)
