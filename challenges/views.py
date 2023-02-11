from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
def monthly_challange_ny_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    if month == "january":
        return HttpResponse("THis is january challanges")
    elif month == "february":
        return HttpResponse("This is february challanges")
    elif month == "march":
        return HttpResponse("This is march challenge")
    else:
        return HttpResponseNotFound("This is not recommended")
    
def challenge_january(request):
    return HttpResponse("<h3>This is January Challanges</h3>")

def challenge_february(request):
    return HttpResponse("<h3>This is February Challenges</h3>")