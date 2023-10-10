from rest_framework.serializers import ModelSerializer
from .models import StadiumModel,BronModel

class StadiumSerializer(ModelSerializer):
    class Meta:
        model = StadiumModel
        fields = ('name', 'adres', 'contact')

class BronSerializer(ModelSerializer):
    class Meta:
        model = BronModel
        fields = ('stadium', 'user', 'start_time', 'end_time', 'price', 'bron_status')


