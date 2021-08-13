from django.db import models

from django.contrib.auth.models import User

class Questionary(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название опроса')
    start_at = models.DateField(auto_now_add=True, verbose_name='Дата старта')
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-start_at']


class Question(models.Model):
    quest_text = models.CharField(max_length=250, verbose_name='Текст вопроса')
    question_type = models.ForeignKey('QuestionType', on_delete=models.PROTECT, null=True, verbose_name='Тип ответов')
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE, null=True, verbose_name='Опрос')

    def __str__(self):
        return self.quest_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    answer_text = models.CharField(max_length=250, verbose_name='Текст ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, verbose_name='Вопрос')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class QuestionType(models.Model):
    title = models.CharField(max_length=250, verbose_name='Тип вариантов ответов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип ответов'
        verbose_name_plural = 'Типы ответов'

class TestQuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE, null=True, verbose_name='Опрос')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, verbose_name='Вопрос')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Элемент прохождения опроса'
        verbose_name_plural = 'Элементы прохождения опроса'



