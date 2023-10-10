from django.contrib import admin

# Register your models here.
from .models import StadiumModel, BronModel

admin.site.register(StadiumModel)
admin.site.register(BronModel)