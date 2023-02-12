from django.urls import path

from . import views

urlpatterns = [
    path("",views.show_month, name="index"),
    path('february',views.challenge_february, name='challenge_february'),
    path("<int:month>", views.monthly_challange_ny_number, name='monthly_challange_ny_number'),
    path("<str:month>", views.monthly_challenge, name='monthly_challenge'),
]
