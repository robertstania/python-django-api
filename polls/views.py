import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question
# Create your views here.
def index(request):
    allQuestions = list(Question.objects.all().values())
    return JsonResponse({"questions": allQuestions}, safe=False)

def getOne(request, id):
    oneQuestion = list(Question.objects.filter(id=id).values())
    return JsonResponse({"question": oneQuestion[0]}, safe=False)

def delete(request, id):
    Question.objects.get(id=id).delete()
    return HttpResponse("deleted!")

@csrf_exempt
def create(request):
    createData = json.loads(request.body)
    Question.objects.create(question_text=createData["question_text"], pub_date=createData["pub_date"])
    return HttpResponse("All good")

@csrf_exempt
def update(request, id):
    updateData = json.loads(request.body)
    Question.objects.filter(id=id).update(question_text=updateData["question_text"], pub_date=updateData["pub_date"])
    return HttpResponse("updated")
