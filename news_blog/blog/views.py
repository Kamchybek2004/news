from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import News
from .form import CommentsForm
import requests


class NewsView(View):
    '''Вывод новостей и информации о погоде'''

    def get(self, request):
        # Получение новостей
        posts = News.objects.all()

        # Получение данных о погоде
        appid = 'c7af500b96b381f1c8085e9f3d18ca04'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
        city = 'Naryn'
        weather_data = {}
        try:
            res = requests.get(url.format(city))
            res.raise_for_status()  # Проверка успешности запроса
            data = res.json()
            weather_data = {
                'city': city,
                'temp': round(data["main"]["temp"] - 273.15, 1),  # Температура в Цельсиях
                'icon': data["weather"][0]["icon"],  # Иконка погоды
                'description': data["weather"][0]["description"],  # Описание погоды
            }
        except requests.exceptions.RequestException as e:
            print(f"Ошибка получения данных о погоде: {e}")

        # Передача данных в шаблон
        context = {
            'post_list': posts,
            'weather': weather_data,
        }
        return render(request, 'blog/index2.html', context)

class Post_DetailView(View):
    '''Отдельная страница записи'''
    def get(self, request, pk):
        posts = News.objects.get(id=pk)
        return render(request, 'blog/post_detail.html', {'post': posts})


class AddComments(View):
    '''Добавление комментарии'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')




