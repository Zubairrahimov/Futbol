from datetime import timezone, timedelta
from rest_framework import generics, views
from rest_framework.response import Response
from .models import StadiumModel, BronModel
from .serializers import StadiumSerializer, BronSerializer
from datetime import timezone, timedelta
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerPermissionClass, AdminPermissionClass, UserPermission

class CRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (AdminPermissionClass, IsAuthenticated)
class CreateStadium(generics.ListCreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated, OwnerPermissionClass)

class CreateBron(generics.ListCreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, UserPermission)

class ALlBrons(generics.ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, OwnerPermissionClass)
class DestroyBronView(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, OwnerPermissionClass)
class AllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated, UserPermission)

from rest_framework import generics
from rest_framework.response import Response
from datetime import timedelta, datetime

from .models import BronModel
from .serializers import BronSerializer
# import datetime

from rest_framework import generics
from rest_framework.response import Response
# from datetime import datetime, timedelta


class AvailableTimeSlotsView(generics.ListAPIView):
    serializer_class = BronSerializer

    def get_queryset(self):
        # Retrieve all reservations for the single stadium
        reservations = BronModel.objects.all()

        # Get the start_date and end_date query parameters from the request
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        # Convert the start_date and end_date to datetime objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Filter reservations that fall within the specified date range
        reservations = reservations.filter(start_time__date__range=[start_date, end_date])

        # Calculate the free time slots within the filtered reservations
        free_time_slots = []
        current_time = start_date

        for reservation in reservations:
            if reservation.start_time > current_time:
                free_time_slots.append({
                    'start_time': current_time,
                    'end_time': reservation.start_time,
                    'available': True,
                    'reserved_by': None,
                })

            current_time = max(current_time, reservation.end_time)
            free_time_slots.append({
                'start_time': reservation.start_time,
                'end_time': reservation.end_time,
                'available': False,
                'reserved_by': reservation.user.username if reservation.user else 'Unknown',
            })

        if current_time < end_date:
            free_time_slots.append({
                'start_time': current_time,
                'end_time': end_date,
                'available': True,
                'reserved_by': None,
            })

        return free_time_slots
    

class ListPollsApiView(generics.ListAPIView):
    serializer_class = BronSerializer
    permission_classes = (OwnerPermissionClass,)
    
    def get_queryset(self):
        return BronModel.objects.filter(bron_status=False)