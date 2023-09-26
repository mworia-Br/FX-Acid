from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def indexfr(request):
    return render(request, 'login&signup.html')

def resetpassword(request):
    return render(request, 'forgotpassword.html')