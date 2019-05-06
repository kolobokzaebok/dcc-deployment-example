from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse


from myapp.models import *
from myapp.forms import *

def index(request):
    return render(request, 'myapp/index.html')

@login_required
def other(request):
    return render(request, 'myapp/other.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        looser_form = LooserForm(data=request.POST)
        if user_form.is_valid() and looser_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            looser = looser_form.save(commit=False)
            looser.user = user
            looser.save()

            registered = True
        else:
            print(user_form.errors, looser_form.errors)
    else:
        user_form = UserForm()
        looser_form = LooserForm()
    return render(request, 'myapp/register.html', {
                            'user_form':user_form,
                            'looser_form':looser_form,
                            'registered':registered
                            })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('sorry')
        else:
            return HttpResponse('wrong username or password')
    else:
        return render(request, 'myapp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))
