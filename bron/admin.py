from django.contrib import admin
from .models import StadiumModel, BronModel

from .forms import BronForm,StadiumForm
# Register your models here.
class BronAdmin(admin.ModelAdmin):
    form = BronForm
    list_display = ('stadium',)
    search_fields = ('stadium',)

class StadiumAdmin(admin.ModelAdmin):
    form = StadiumForm
    list_display = ('name',)
    search_fields = ('name',)  


admin.site.register(StadiumModel, StadiumAdmin )
admin.site.register(BronModel, BronAdmin)
