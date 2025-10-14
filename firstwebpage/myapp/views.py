from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    # Возвращаем рендер шаблона index.html
    return render(request, 'index.html')

def hello(request):
    # Возвращаем рендер шаблона static_handler.html
    return render(request, 'static_handler.html')
