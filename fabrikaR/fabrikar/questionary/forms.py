from django import forms
from django.contrib.auth.models import User
from .models import Questionary, Question, Answer, TestQuest




#  ModelChoiceField Позволяет выбор единственного объекта модели, имеет смысл при отображении внешнего ключа.
class TestQuestCheckboxForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='user', queryset=User.objects.all(), widget=forms.HiddenInput)
    questionary = forms.ModelChoiceField(label='user', queryset=Questionary.objects.filter(pk=48))
    question = forms.ModelChoiceField(label='user', queryset=Question.objects.filter(pk=22))
    answers_set = forms.ModelMultipleChoiceField(queryset=Answer.objects.all(), widget=forms.CheckboxSelectMultiple())
    # questionary = Questionary.objects.get(pk = )
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # choice_field.choices
    class Meta:
        model = TestQuest
        fields = '__all__'
        widgets = {

        }

    def save_checkbox_question(self):
        item_form = self.save(commit=False)
        a = self.data.getlist('answers_set')
        for item in a:
            b = Answer.objects.get(pk=item)
            test_quest = TestQuest(answer=b,
                                    questionary=self.cleaned_data['questionary'],
                                    question=self.cleaned_data['question'],
                                    user=self.cleaned_data['user'])
            test_quest.save()


class TestQuestTextForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='user', queryset=User.objects.all())
    questionary = forms.ModelChoiceField(label='user', queryset=Questionary.objects.filter(pk=48))
    question = forms.ModelChoiceField(label='user', queryset=Question.objects.filter(pk=22))
    answer = forms.CharField()
    # questionary = Questionary.objects.get(pk = )
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # choice_field.choices
    class Meta:
        model = TestQuest
        fields = '__all__'
        widgets = {

        }
class TestQuestRadioForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='user', queryset=User.objects.all())
    questionary = forms.ModelChoiceField(label='user', queryset=Questionary.objects.filter(pk=48))
    question = forms.ModelChoiceField(label='user', queryset=Question.objects.filter(pk=22))
    answer = forms.ModelChoiceField(queryset=Answer.objects.filter(pk=23), widget=forms.CheckboxSelectMultiple())
    # questionary = Questionary.objects.get(pk = )
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    # choice_field.choices
    class Meta:
        model = TestQuest
        fields = '__all__'
        widgets = {

        }

class AddQuestionaryForm(forms.ModelForm):
    class Meta:
        model = Questionary
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'style': 'max-width : 300px'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'style': 'max-width : 300px'}),
        }

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quest_text', 'question_type']
        widgets = {
            'quest_text': forms.TextInput(attrs={'class':'form-control', 'style': 'max-width : 300px'}),
            'question_type': forms.Select(attrs={'class': 'form-control', 'rows': 5, 'style': 'max-width : 300px'}),
        }

class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.TextInput(attrs={'class':'form-control', 'style': 'max-width : 300px'}),
        }

#  ModelChoiceField Позволяет выбор единственного объекта модели, имеет смысл при отображении внешнего ключа.
# 28.07.2021
# class TestQuestCheckboxForm(forms.ModelForm):
#     user = forms.ModelChoiceField(label='user', queryset=User.objects.all())
#     questionary = forms.ModelChoiceField(label='user', queryset=Questionary.objects.filter(pk=48))
#     question = forms.ModelChoiceField(label='user', queryset=Question.objects.filter(pk=22))
#     answers_set = forms.ModelMultipleChoiceField(queryset=Answer.objects.all(), widget=forms.CheckboxSelectMultiple())
#     # questionary = Questionary.objects.get(pk = )
#     # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
#     # choice_field.choices
#     class Meta:
#         model = TestQuest
#         fields = '__all__'
#         widgets = {
#
#         }
#
#     def save_checkbox_question(self):
#         item_form = self.save(commit=False)
#         a = self.data.getlist('answers_set')
#         for item in a:
#             b = Answer.objects.get(pk=item)
#             test_quest = TestQuest(answer=b,
#                                     questionary=self.cleaned_data['questionary'],
#                                     question=self.cleaned_data['question'],
#                                     user=self.cleaned_data['user'])
#             test_quest.save()
