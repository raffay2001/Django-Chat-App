from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Function for rendering the Index Page 
@login_required(login_url='/login/')
def frontpage(request):
    return render(request, 'core/frontpage.html')


# Function for dealing with the Registration of the User
def sigunp(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('frontpage'))
    
    else:
        form = SignUpForm()
        context = {
            'form' : form
        }
        # if its a POST request 
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            
            if form.is_valid():
                user = form.save()          # it returns the newly created User object .
                login(request, user)        # login() function takes two params { 1. request }, { 2. < User Object > }  
                return HttpResponseRedirect(reverse('frontpage'))
            else:
                message = form.errors
                messages.error(request, message)
                return HttpResponseRedirect(reverse('signup'))
        
        # if its a GET request 
        else:
            return render(request, 'core/signup.html', context)


# Funcion for logging the user in 
def signin(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('frontpage'))
    
    else:
        # if its a GET request 
        if request.method == 'GET':
            return render(request, 'core/login.html', {})
        
        # if its a POST request 
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('frontpage'))
            else:
                messages.error(request, 'Invalid Username or Password')
                return HttpResponseRedirect(reverse('login'))
