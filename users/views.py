from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.models import User
from.forms import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def registerForm(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect('login')
        else:
            messages.info(request, "Password does'nt match")
            return redirect('register')
    return render(request, 'users/register.html')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Checking if the user already exist
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User dosent exist')
        #So if the user exist, we authenticate them
        user = authenticate(request, username=username, password=password)

        if user is not None: # if the user is true
            login(request, user)
            return redirect('home')
        else:
              messages.warning(request, "Username OR password dosen't exist")
    return render(request, 'users/login.html')



def logoutPage(request):
    logout(request)
    return render(request, 'users/logout.html')


def profilePage(request):
    if request.method == 'POST':
        user_form = UserUpdate(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(), profile_form.save()
            messages.success(request, 'Update Successfull')
            return redirect('profile')
    else:
        user_form = UserUpdate(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)