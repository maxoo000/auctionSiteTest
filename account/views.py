from django.shortcuts import render, HttpResponse, redirect, reverse

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User
from .models import Account

import json

# Create your views here.
def accountPage(request):
    return HttpResponse("Account page")


def accountLogin(request):
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    return render(request, 'account/login_page.html')


def accountRegister(request):
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    return render(request, 'account/register_page.html')

@login_required
def logoutView(request):
    logout(request)
    return redirect(reverse('index'))

@require_POST
def register(request):
    all_good = True
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    username = request.POST['username']
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    email = request.POST['email']
    password = request.POST['password']
    register_errors = {}
    try:
        User.objects.get(email=email)
        print("Email already in use")
        all_good = False
        register_errors["email"] = True
        # return redirect(reverse('accountRegister'))
    except:
        pass

    try:
        User.objects.get(username=username)
        print("Username already in use")
        all_good = False
        register_errors["username"] = True
        # return redirect(reverse('accountRegister'))
    except:
        pass

    if len(password) < 6:
        print("Password  needs to have at least 6 characters")
        all_good = False
        register_errors["password"] = True
        # return redirect(reverse('accountRegister'))

    # All good

    if all_good:
        new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
        new_account = Account.objects.create(user=new_user)
        # print("Account has been created")
        try:
            auth_user = authenticate(request, username=username, password=password)
            login(request, user=auth_user)
            # print("Logged in")
        except Exception as E:
            print(E)
        return HttpResponse("reg")
    else:
        register_errors = json.dumps(register_errors)
        return HttpResponse(register_errors)

@require_POST
def loginView(request):
    # print("PROVERA")
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    # print("START")
    username = request.POST['username']
    password = request.POST['password']

    try:
        # print("PRE AUTH")
        auth_user = authenticate(request, username=username, password=password)
        # print("POST AUTH")
        if auth_user is not None:
            # print("PRE LOGIN")
            login(request, user=auth_user)
            return HttpResponse("log")
            # print("POST LOGIN")
        else:
            # print("LOGIN FAIL")
            return HttpResponse("fail")
            # return render(request, 'account/login_page.html', {"login_fail": True})
    except Exception as E:
        print(E)
        return HttpResponse("err")
        # return render(request, 'account/login_page.html', {"login_error": True})



