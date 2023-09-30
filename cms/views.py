from typing import Any
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponse, request

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            messages.success(request, "Congratulations! Registration Successful!")
            form.save()
        else:
            form = RegistrationForm()
            return render(request, 'register.html', {'form': form})
        
        return redirect('cms:login')


def IndexView(request):
    return render(request, 'index.html')

def accounts(request):
    return render(request, 'login&signup.html')

def resetpassword(request):
    return render(request, 'forgotpassword.html')

def ServiceView(request):
    return render(request, 'service.html')

def SystemView(request):
    return render(request, 'project.html')

def ContactView(request):
    return render(request, 'contact.html')