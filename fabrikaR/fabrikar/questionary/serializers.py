from rest_framework import serializers

from .models import Questionary, Question, Answer, QuestionType

class QuestionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionary
        fields = ('id', 'title', 'start_at', 'end_date', 'description')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'quest_text', 'question_type', 'questionary')

class QuestionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionType
        fields = ('id', 'title')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text', 'question')