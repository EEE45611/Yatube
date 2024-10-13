import django.core.handlers.wsgi
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('какой то текст')
def index2(request):
    return HttpResponse('''вкусная морожка
                       шкоколадная морожка
                        крутттая морожка''')
def index3(request:django.core.handlers.wsgi.WSGIRequest,id):

    return HttpResponse('мороженное номер'+id)
def index4(request:django.core.handlers.wsgi.WSGIRequest,id):

    return HttpResponse(f'your ip-{request.META["HTTP_HOST"]}ты перешел с сайта {request.META.get("HTTP_REFERER")}')
# Create your views here.
