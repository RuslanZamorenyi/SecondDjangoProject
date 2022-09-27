from django.http import HttpResponse, FileResponse, HttpResponseRedirect, \
    HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static

from django.views import View

from django.template import loader


def main(request):
    test_template = loader.render_to_string("main.html")

    return HttpResponse(test_template)


def text(request):
    return HttpResponse("Люк Скайвокер — один із головних персонажів всесвіту «Зоряних воєн», джедай,"
                        " син сенатора з Набу Падме Амідали Наберріє та лицаря-джедая Енакіна Скайвокера. ")


def file(request):
    return HttpResponse("Лея Органа – дочка лицаря-джедая Енакіна Скайвокера та сенатора Падме Амідали Наберріє. ")


def redirect(request):
    return HttpResponse("Ган Соло — пілот космічного корабля «Тисячолітній сокіл». Його бортмеханіком і"
                        " другим пілотом є вукі на Чубакка. ")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)

def test(request):
    return HttpResponse("lesson_3")