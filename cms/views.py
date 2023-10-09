from typing import Any
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views import View
from django.http import HttpResponse, JsonResponse, request
from django.contrib.auth.decorators import login_required
from .models import Service, System, SystemData, Consent

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

@login_required
def ServiceView(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

@login_required
def SystemView(request):
    traders = System.objects.all()
    return render(request, 'project.html', {'traders': traders})

@login_required
def ContactView(request):
    return render(request, 'contact.html')

def chart_data(request):
    data = SystemData.objects.all()  # Replace YourModel with your actual model
    labels = [item.date for item in data]
    values = [item.roi for item in data]

    chart_data = {
        'label': 'ROI',
        'labels': labels,
        'values': values,
        'chart_type': 'line' # any chart type line, bar, ects
    }
    return JsonResponse(chart_data)

def chart_view(request):
    return render(request, 'chart.html')