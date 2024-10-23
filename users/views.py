from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from users.forms import UserForm

def login(request):
    context = {'title': 'Login'}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('web:home'))

        context.update({
            'error': True,
            'message': 'Invalid username or password',
        })

    return render(request, 'users/login.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:home'))

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            User.objects.create_user(
                username=instance.username,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name,
                password=instance.password
            )
             
            user = authenticate(request, username=instance.username, password=instance.password)
            auth_login(request, user)

            return HttpResponseRedirect(reverse('web:home'))
    else:
        form = UserForm()
        context = {
            'title': 'Signup',
            'form': form
        }
    return render(request, 'users/signup.html', context=context)