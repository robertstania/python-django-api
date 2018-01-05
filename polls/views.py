import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ast
from .models import Question
# Create your views here.
def index(request):
    allQuestions = list(Question.objects.all().values())
    return JsonResponse({"questions": allQuestions}, safe=False)

@csrf_exempt
def create(request):
    createData = json.loads(request.body)
    Question.objects.create(question_text=createData["question_text"], pub_date=createData["pub_date"])
    return HttpResponse("All good")
