from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
    else:
        messages.add_message(
            request, messages.ERROR,
            'The username and/or password entered is not valid. Please try again.'
        )
    return redirect(reverse('home'))


def logout(request):
    auth_logout(request)
    return redirect(reverse('home'))


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(reverse("home"))
        messages.add_message(request, messages.ERROR, 'Error')
        return redirect(reverse("register"))
