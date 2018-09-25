from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from myblogback.froms import UserLoginForm


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        # 引入表单验证，验证用户名是否注册
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # 校验用户名和密码，判断返回的对象是否为空，不为空就是user对象
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['userpwd'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('myblogback:article'))
            else:
                return render(request, 'login.html', {'error': '密码错误'})
        else:
            return render(request, 'login.html', {'form': form})


def article(request):
    if request.method == "GET":
        return render(request, 'article.html')


def add_article(request):
    if request.method == "GET":
        return render(request, 'add_article.html')