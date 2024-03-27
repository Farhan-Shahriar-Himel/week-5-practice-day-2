from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from album.models import Album
# Create your views here.
def profile(request):
    return render(request, 'userhome.html')


def register(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('profile')
    form = forms.CreateUserForm()
    return render(request, 'registration.html', {'form': form})


def userLogIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in successfully")
                return redirect('profile')
            else:
                messages.warning(request, "wrong username or password")
                return redirect('homepage')
    
    form = AuthenticationForm()
    return render(request, 'registration.html', {'form': form})


def profile(request):
    data = Album.objects.all()
    return render(request, 'userhome.html', {'data': data})


def logOut(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('homepage')