from django.urls import path
from .views import (CreateBron, CreateStadium, ALlBrons, 
    AvailableTimeSlotsView
    )


urlpatterns = [
    path('create/stadium/', CreateStadium.as_view()),
    path('create/bron/', CreateBron.as_view()),
    path('brons/', ALlBrons.as_view()),
    path('freestadiums/', AvailableTimeSlotsView.as_view()),

]