from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

def accounts(request):
    return render(request, 'login&signup.html')

def resetpassword(request):
    return render(request, 'forgotpassword.html')

def ServiceView(request):
    return render(request, 'project.html')

def SystemView(request):
    return render(request, 'service.html')

def ContactView(request):
    return render(request, 'contact.html')