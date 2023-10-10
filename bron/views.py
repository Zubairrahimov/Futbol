from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StadiumModel,BronModel
from .serializers import StadiumSerializer,BronSerializer
from permissions import OwnerPermissionClass,AdminPermissionClass,UserPermission
from rest_framework.permissions import IsAuthenticated



#                admin views

class CreatePollsAPiView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class DeleteBron(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class AllBronsView(generics.APIView):
    def get(self,request,*args,**kwargs):
        try:
            print(kwargs["bron_status"])
            all_bron = BronModel.objects.filter(bron_status=kwargs["bron_status"].title())
            serializer = BronSerializer(all_bron,many=True)
            permission_classes = (IsAuthenticated,AdminPermissionClass)
            return Response(serializer.data)
        except:
            return Response({"message":"please enter true value only"})

#                 Owner

class BronsView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            print(kwargs["bron_status"])
            all_bron = BronModel.objects.filter(bron_status=kwargs["bron_status"].title())
            serializer = BronSerializer(all_bron,many=True)
            permission_classes = (IsAuthenticated,OwnerPermissionClass)
            return Response(serializer.data)
        except:
            return Response({"message":"please enter true value only"})

class CreatePollsAPiView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,OwnerPermissionClass)

class DeleteBron(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,OwnerPermissionClass)



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