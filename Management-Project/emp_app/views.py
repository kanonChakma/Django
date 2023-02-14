from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("hello")
    return render(request, 'emp_app/index.html')

def add_emp(request):
    return render(request, 'emp_app/add_emp.html')

def remove_emp(request):
    return render(request, 'emp_app/remove_emp.html')

def view_emp(request):
    return render(request, 'emp_app/view_emp.html')

def filter_emp(request):
    return render(request, 'emp_app/filter_emp.html')