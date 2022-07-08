from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            # user.first_name = 'farhad3dd'
            # user.last_name = 'mohebbi'
            user.save()
            messages.success(request, 'Register Successfully', 'success')
            return redirect('home')

    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password', 'danger')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out successfully', 'success')
    return redirect('home')