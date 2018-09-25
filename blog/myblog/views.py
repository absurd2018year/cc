
from django.shortcuts import render

from myblog.models import Article


def index(request):
    if request.method == "GET":
        articles = Article.objects.all()
        return render(request, 'index.html',{'articles':articles})


def about(request):
    if request.method == "GET":
        return render(request, 'about.html')


def info(request):
    if request.method == "GET":
        return render(request, 'info.html')

