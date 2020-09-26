"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

from django.shortcuts import HttpResponse, render,redirect

def login(request):
    # return HttpResponse('login') # 这里返回的是'login字符串' 这里也只能写字符串，如果需要加网址，就要render
    if request.method == "GET":  # 一般的请求网页的method 都是GET类型
        return render(request, 'login.html')
    elif request.method == "POST": # 点击发送按钮后的数据都是POST形式
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u=='admin' and p=='123123':
            # 登录成功
            return redirect('/index/')
        else:
            # 登录不成功就刷新这个页面
            return render(request, 'login.html',{'msg':'username or password incorrect'})

def index(request):
    return render(request,'index.html')

urlpatterns = [
     #url(r'^admin/', admin.site.urls),
    url(r'^login/',login),
    url(r'^index/',index),
    url(r'^classes/',views.classes),
    url(r'^addClass/',views.addClass),
    url(r'^delClass/',views.delClass),
    url(r'^editClass/',views.editClass),
    url(r'^students/',views.students),
    url(r'^addStudent/',views.addStudent),
    url(r'^editStudent/',views.editStudent),

]
