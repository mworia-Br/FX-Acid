from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
import pandas as pd
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

def excel_preview(request, system_id):
    system = get_object_or_404(System, id=system_id)

    if system.excel_file:
        excel_file_path = system.excel_file.path

        # Specify the number of header rows to skip (assuming the header is in the first four rows)
        skiprows = 4

        # Read the Excel file, skipping the header rows
        df = pd.read_excel(excel_file_path, skiprows=skiprows)

        # Customize the HTML conversion
        html_table = df.to_html(
            classes='table table-striped',
            na_rep='',  # Replace NaN values with an empty string
            index=False,  # Do not display the DataFrame index
            col_space=20,  # Set the column space for better readability
            bold_rows=False,  # Do not bold the header row
            justify='left',  # Justify content to the left
            border=0  # Set border to 0 for a cleaner look
        )

        context = {'html_table': html_table, 'system_name': system.name}
        return render(request, 'excel_preview.html', context)
    else:
        return render(request, 'excel_not_found.html', {'system_name': system.name})