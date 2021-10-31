from django.shortcuts import render
from django.views import View


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class LogIn(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)


class Register(View):
    def get(self, request):
        context = {}
        return render(request, 'register.html', context=context)