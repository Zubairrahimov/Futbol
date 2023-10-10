from django.shortcuts import render,get_object_or_404
from rest_framework import generics, views
from rest_framework.response import Response
from .models import StadiumModel,BronModel
from .serializers import StadiumSerializer,BronSerializer
from .permissions import OwnerPermissionClass,AdminPermissionClass,UserPermission
from rest_framework.permissions import IsAuthenticated

#                admin views

class AdminCreateAPiView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class AdminDeleteBron(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class AdminAllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class UpdateStatusPollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

    #      Owner views

class OwnerCreatePollsAPiView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,OwnerPermissionClass)

class OwnerDeleteBron(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,OwnerPermissionClass)

class OwnerAllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,)

class OwnerUpdateStatusPollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

#                      user views

class StadiumDetailUserView(generics.RetrieveAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,UserPermission)

class StadiumBronUserView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,UserPermission)

class AllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,UserPermission)
    
class ListPollsApiView(generics.ListAPIView):
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return BronModel.objects.filter(status=False)
    

