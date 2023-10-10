from django.urls import path
from .views import (CreateBron, CreateStadium, ALlBrons, 
    AvailableTimeSlotsView, ListPollsApiView, CRUDView, DestroyBronView, 

    )


urlpatterns = [
    path('create/stadium/', CreateStadium.as_view()),
    path('create/bron/', CreateBron.as_view()),
    path('brons/', ALlBrons.as_view()),
    path('freestadiums/', AvailableTimeSlotsView.as_view()),
    path('frst/', ListPollsApiView.as_view()),
    path('crud/', CRUDView.as_view()),
    path('stadium/destroy/', DestroyBronView.as_view()),
]