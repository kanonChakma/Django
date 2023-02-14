from django.http import HttpResponse
from django.shortcuts import render

from .models import Department, Employee, Role


# Create your views here.
def index(request):
    # return HttpResponse("hello")
    return render(request, 'emp_app/index.html')


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])

        new_emp = Employee(first_name=first_name, last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone)
        new_emp.save()
        return HttpResponse("Employee added Successfully")

    elif request.method == 'GET':
        return render(request, 'emp_app/add_emp.html')
    else:
       return HttpResponse("Employee not added") 

    


def remove_emp(request):
    return render(request, 'emp_app/remove_emp.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'emp_app/view_emp.html',context)

def filter_emp(request):
    return render(request, 'emp_app/filter_emp.html')
 