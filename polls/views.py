from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Choice, Question

def index(request):
    questoes = Question.objects.all()
    questoes_str = str(questoes[0].question_text)

    return HttpResponse("Olá, mundo. Você está no índice de pesquisas.<br>" + questoes_str)