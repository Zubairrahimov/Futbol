from django.urls import path
from .views import *



urlpatterns = [
    #   ADMIN api

    path('Admincreate/',AdminCreateAPiView.as_view()),
    path('Amindetsroy/<int:pk>/',AdminDestroyBronView.as_view()),
    path('AdminAllStadion/', AdminAllStadiumView.as_view()),
    path('Adminbrons/',AdminAllBrons.as_view()),
    path('Aminupdates/<int:pk>/',UpdateStatusPollsView.as_view()),


    # owner api
    path('Ownercreatebron/',OwnerCreateBronAPiView.as_view()),
    path('Ownercreatestadion/',OwnerCreateStadium.as_view()),
    path('Ownerdestroy/<int:pk>',OwnerDestroyBronView.as_view()),
    path('OwnerAllbron/', OwnerAllBrons.as_view()),
    path('OwerAllstadion/',OwnerAllStadiumView.as_view()),
    path('OwnerUpdateBron/<int:pk/',OwnerUpdateBronPollsView),

    # user api
    path('Userdetail/<int:pk>',StadiumDetailUserView.as_view()),
    path('Userbrone',StadiumBronUserView.as_view()),
    path('userAll/',AllStadiumView.as_view()),
    path(' ListPolls/',ListPollsApiView.as_view())

]