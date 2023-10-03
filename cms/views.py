from typing import Any
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from .models import Service, System, SystemData

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

@login_required
def IndexView(request):
    services = Service.objects.all()
    traders = System.objects.all()
    return render(request, 'index.html', {'services': services, 'traders': traders})

def accounts(request):
    return render(request, 'login&signup.html')

def resetpassword(request):
    return render(request, 'forgotpassword.html')

def ServiceView(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def SystemView(request):
    traders = System.objects.all()
    return render(request, 'project.html', {'traders': traders})

def ContactView(request):
    return render(request, 'contact.html')