from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    obj = {
        "priority": 100, "task": "скласти список справ",
        "priority": 150, "task": "Вчити Django'",
        "priority": 1, "task": "'Подумати про сенс життя"
    }

    context = {
        "obj": obj
    }

    return render(request, "lesson.html", context)

def test(request):
    return HttpResponse("lesson_3_1")