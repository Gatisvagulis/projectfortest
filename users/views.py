from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('welcome')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username=username)
        except:
            messages.error(request, 'Username dose not exist')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Password is inncorect')

    return render(request, 'users/login_form.html')


def logoutPage(request):
    logout(request)
    messages.success(request, 'User was loged out')
    return redirect('login')


# @login_required(login_url="login")