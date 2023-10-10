from django.urls import path
from .views import *

urlpatterns = [
    #   ADMIN api

    path('Admincreate/',AdminCreateAPiView.as_view()),
    path('Amindelete/<int:pk>',AdminDeleteBron.as_view()),
    path('AdminAllStadion/', AdminAllStadiumView.as_view()),


    # owner api
    path('Admincreate/',OwnerCreatePollsAPiView.as_view()),
    path('Amindelete/<int:pk>',OwnerDeleteBron.as_view()),
    path('AdminAll/', OwnerAllStadiumView.as_view()),

    # user api
    path('Userdetail/<int:pk>',StadiumDetailUserView.as_view()),
    path('Userbrone',StadiumBronUserView.as_view()),
    path('userAll/',AllStadiumView.as_view())
]