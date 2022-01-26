from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

from django.contrib.auth import authenticate, login
from .forms import CreateAdminForm

def login_view(request):
    msg = None
    
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show_books')
        else:
            msg = "Incorrect credentials"
            print('User is ', user)
    
    context = {
        'message' : msg
    }
    return render(request, 'login.html', context)


def register(request):
    msg = None

    if request.method == "POST":
        form = CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
        else:
            msg = 'Password Does\'t match or is too easy'
    context = {
        'message' : msg
    }
    return render(request, 'signup.html', context)