from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import *
from django.forms import formset_factory

from django.http import HttpResponseRedirect

from .forms import AddQuestionaryForm, AddQuestionForm, AddAnswerForm, TestQuestCheckboxForm
from .models import Questionary, Question, Answer, TestQuest

class QuestionaryViewSet(viewsets.ModelViewSet):
    queryset = Questionary.objects.all().order_by('start_at')
    serializer_class = QuestionarySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

class QuestionTypeViewSet(viewsets.ModelViewSet):
    queryset = QuestionType.objects.all().order_by('id')
    serializer_class = QuestionTypeSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-question')
    serializer_class = AnswerSerializer

def quest(request, questionary_id):
    questionary = Questionary.objects.get(pk=questionary_id)
    questions = Question.objects.filter(questionary=questionary)
    # answers = Answer.objects.filter(question__in=questions)
    answers = Answer.objects.all()
    ArticleFormSet = formset_factory(TestQuestCheckboxForm, extra=2)
    if request.method == 'POST':
        # for item in :
        form = TestQuestCheckboxForm(request.POST)
        # form.questionary = questionary
        a = form.data.getlist('answers_set')
        print(a)
        if form.is_valid():
            form.save_checkbox_question()
    else:
        form = TestQuestCheckboxForm()
    # print(form)
    context = {'questionary': questionary, 'questions': questions, 'answers': answers, 'form': form,
               'ArticleFormSet': ArticleFormSet}
    return render(request, 'questionary/quest.html', context)

# 28/07/2021
# def quest(request, questionary_id):
#     questionary = Questionary.objects.get(pk=questionary_id)
#     questions = Question.objects.filter(questionary=questionary)
#     # answers = Answer.objects.filter(question__in=questions)
#     answers = Answer.objects.all()
#     ArticleFormSet = formset_factory(TestQuestCheckboxForm, extra=2)
#     if request.method == 'POST':
#         # for item in :
#         form = TestQuestCheckboxForm(request.POST)
#         # form.questionary = questionary
#         a = form.data.getlist('answers_set')
#         print(a)
#         if form.is_valid():
#             form.save_checkbox_question()
            # for item in a:
            #     form = TestQuestCheckboxForm(request.POST)
            #     post_form = form.save(commit=False)
            #     post_form2 = form.save(commit=False)
            #     b = Answer.objects.get(pk=item)
            #     print(form.is_bound)
            #     print(item)
            #     print(post_form)
            #     # user = request.user
            #     post_form.answer = b
            #     post_form2.answer = b
            #     post_form.save()
            #     print(TestQuest.answer)
            #     post_form2.save()
            #     print(TestQuest.answer)

    # else:
    #     form = TestQuestCheckboxForm()
    # # print(form)
    # context = {'questionary': questionary, 'questions': questions, 'answers': answers, 'form': form,
    #            'ArticleFormSet': ArticleFormSet}
    # return render(request, 'questionary/quest.html', context)



# def quest(request, questionary_id):
#     questionary = Questionary.objects.get(pk=questionary_id)
#     questions = Question.objects.filter(questionary=questionary)
#     # answers = Answer.objects.filter(question__in=questions)
#     answers = Answer.objects.all()
#     ArticleFormSet = formset_factory(TestQuestCheckboxForm, extra=2)
#     if request.method == 'POST':
#         # for item in :
#         form = TestQuestCheckboxForm(request.POST)
#         # form.questionary = questionary
#         a = form.data.getlist('answers_set')
#         print(a)
#         for item in a:
#             if form.is_valid():
#                 # user = request.user
#                 answer = Answer.objects.get(pk=item)
#                 questionary = form.cleaned_data['questionary']
#                 question = form.cleaned_data['question']
#                 user = form.cleaned_data['user']
#                 TestQuest.objects.create(user=user, questionary=questionary, question=question, answer=answer)
#                     # form.save()
#     else:
#         form = TestQuestCheckboxForm()
#     # print(form)
#     context = {'questionary': questionary, 'questions': questions, 'answers': answers, 'form': form, 'ArticleFormSet': ArticleFormSet}
#     return render(request, 'questionary/quest.html', context)

# def test_questionary(request, questionary_id):
#     if request.method == 'POST':
#         test_quest_form = TestQuestForm(request.POST)
#         questionary = Questionary.objects.get(pk=questionary_id)
#         questions = Question.objects.filter(questionary=questionary)
#         answers = Answer.objects.filter(question__in=questions)
#             if test_quest_form.is_valid():
#                 post_quest = test_quest_form.save(commit=False)
#                 post_quest.user = request.user
#                 post_quest.questionary = questionary.pk
#                 post_quest.question = questions.pk
#                 post_quest.save()
#     else:
#         test_quest_form = TestQuestForm()
#     context = {'quest_form': test_quest_form}
#     return render(request, 'questionary/quest.html', context)

def add_quest(request):
    if request.method == 'POST':
        questionary_form = AddQuestionaryForm(request.POST)
        question_form = AddQuestionForm(request.POST)
        answer_form = AddAnswerForm(request.POST)
        if questionary_form.is_valid():
            post_questionary = questionary_form.save(commit=False)
            post_questionary.save()
            if question_form.is_valid():
                    post_question = question_form.save(commit=False)
                    post_question.questionary = post_questionary
                    post_question.save()
                    if answer_form.is_valid():
                        post_answer = answer_form.save(commit=False)
                        post_answer.question = post_question
                        post_answer.save()
            questionary_form = AddQuestionaryForm()
            question_form = AddQuestionForm()
            answer_form = AddAnswerForm()
            return HttpResponseRedirect('/add_questionary')
    else:
        questionary_form = AddQuestionaryForm()
        question_form = AddQuestionForm()
        answer_form = AddAnswerForm()
    context = {'questionary_form': questionary_form, 'question_form': question_form, 'answer_form': answer_form}
    return render(request, 'questionary/add_questionary.html', context)


def add_questionary(request):
    if request.method == 'POST':
        questionary_form = AddQuestionaryForm(request.POST)
        if questionary_form.is_valid():
            post_questionary = questionary_form.save(commit=False)
            post_questionary.save()
            questionary = post_questionary
            return HttpResponseRedirect('/add_questions')
    else:
        questionary_form = AddQuestionaryForm()
    context = {'questionary_form': questionary_form}
    return render(request, 'questionary/add_questionary.html', context)


def add_questions(request):
    if request.method == 'POST':
        question_form = AddQuestionForm(request.POST)
        answer_form = AddAnswerForm(request.POST)
        if question_form.is_valid():
            post_question = question_form.save(commit=False)
            # post_question.questionary = questionary
            post_question.save()
            if answer_form.is_valid():
                post_answer = answer_form.save(commit=False)
                post_answer.question = post_question
                post_answer.save()

        question_form = AddQuestionForm()
        answer_form = AddAnswerForm()
        return HttpResponseRedirect('/add_questions')
    else:

        question_form = AddQuestionForm()
        answer_form = AddAnswerForm()
    context = {'question_form': question_form, 'answer_form': answer_form}
    return render(request, 'questionary/add_questions.html', context)

def list_questionary(request):
    questionary = Questionary.objects.order_by('-start_at')
    context = {'questionary': questionary, 'title': 'Опросы'}
    return render(request, 'questionary/list_questionary.html', context)
