from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user=authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user  is not None:
            login(request, user)
            return redirect('home')
        return redirect('login')

def Logout_view(request):
    logout(request)
    return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('confirm_password'):
            users=User.objects.filter(username=request.POST.get('username'))
            if users.exists():
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password')
                )
                login(request, user)
                return redirect('home')
        return redirect('register')

