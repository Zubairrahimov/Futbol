from datetime import timezone, timedelta
from rest_framework import generics, views
from rest_framework.response import Response
from .models import StadiumModel, BronModel
from .serializers import StadiumSerializer, BronSerializer
from datetime import timezone, timedelta, datetime
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerPermissionClass, AdminPermissionClass, UserPermission

# ----------------- admin views ----------------

class AdminAllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class AdminCreateAPiView(generics.ListCreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class AdminDestroyBronView(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class AdminAllBrons(generics.ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass)

class UpdateStatusPollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

#------------------- Owner views ----------------------

class OwnerCreateBronAPiView(generics.ListCreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,OwnerPermissionClass)

class OwnerCreateStadium(generics.ListCreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated, OwnerPermissionClass)

class OwnerAllBrons(generics.ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, OwnerPermissionClass)

class OwnerDestroyBronView(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,OwnerPermissionClass)

class OwnerAllStadiumView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,)

class OwnerUpdateBronPollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

#--------------------- user views ------------------------

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

#admin va stadion egasi tomonidan tekshirilgan bron qilinmagan vaqtlar chiqadi

class ListPollsApiView(generics.ListAPIView):
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return BronModel.objects.filter(bron_status=False)



class AvailableTimeSlotsView(generics.ListAPIView):
    serializer_class = BronSerializer

    def get_queryset(self):
        reservations = BronModel.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        reservations = reservations.filter(start_time__date__range=[start_date, end_date])
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