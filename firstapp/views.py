from django.shortcuts import render
from django.http import HttpResponse as fun
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse as render_2  # то же самое что и render


def index(request):
    return render_2(request, 'firstapp/home.html')
    # # data = {'header': 'Передача параметров в шаблон Django',
    # #         'message': 'Загружен шаблон templates/firstapp/index_app.html'}
    # # return render(request, 'firstapp/index_app1.html', context=data)
    # header = 'Персональные данные'
    # langs = ['Английский', 'Немецкий', 'Испанский']
    # user = {'name': 'Влад', 'age': '28'}
    # addr = ('Виноградная', 23, 45)
    # data = {'header': header, 'langs': langs, 'user': user, 'addr': addr}
    # return render(request, 'index.html', context=data)


def about(request):
    return fun('<h2>О сайте</h2>')


def contact(request):
    return HttpResponseRedirect('/about')


def details(request):
    return HttpResponsePermanentRedirect('/')


def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return fun(output)


def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Влад')
    output = '<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>'.format(id, name)
    return fun(output)
# Create your views here.