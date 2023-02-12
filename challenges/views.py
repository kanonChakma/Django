from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

challenges = {
    "january": "<h2>This is january challenges</h2>",
    "february":"<h2>This is february challenges</h2>",
    "march":"<h2>This is march challenges</h2>",
    "april": "<h2>This is april challenges</h2>",
    "may": "<h2>This is may challenges</h2>",
    "june": "<h2>This is june challenges</h2>",
    "july":"<h2>This is jully challenges</h2>",
    "august": "<h2>THis is august challenges</h2>",
    "september": "<h2>This is september challenges</h2>",
    "october":"<h2>This is october challnges</h2>",
    "november": "<h2>This is november challenges</h2>",
    "december": "<h2>This is december challenges</h2>"
}

# Create your views here.
def monthly_challange_ny_number(request, month):
    monthList = list(challenges.keys())
    if month > len(monthList):
        return HttpResponseNotFound("This page is not found!!!")

    redirect_month = monthList[month]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def show_month(request):
    months = list(challenges.keys())
    month_list = ""
    for month in months:
        capitalized_month = month.capitalize()
        redirect_path = reverse("monthly_challenge",args=[month])
        month_list += f"<li><a href=\"{redirect_path}\"><h3>{capitalized_month}</h3></a><li>"

    show_list = f"<ul>{month_list}</ul>"
    return HttpResponse(show_list)


def monthly_challenge(request, month):
    try:
        challenge_response = challenges[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_response,
            "month_name": month.capitalize() 
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This is not recommended") 

def challenge_january(request):
    return HttpResponse("<h3>This is January Challanges</h3>")

def challenge_february(request):
    return HttpResponse("<h3>This is February Challenges</h3>")






