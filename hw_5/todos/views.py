from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .models import Todo
from .forms import TodoForm

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, passwornd=password)
        if user is not None:
            login(request, user)
            return redirect('todos_list')
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

