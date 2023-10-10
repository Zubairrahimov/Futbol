from django import forms
from bron.models import StadiumModel, BronModel
class BronForm(forms.ModelForm):
    stadium_uz = forms.CharField()
    stadium_ru = forms.CharField()
    stadium_en = forms.CharField()

    class Meta:
        model = BronModel
        exclude = ('stadium',)


class StadiumForm(forms.ModelForm):

    name_uz = forms.CharField()
    name_ru = forms.CharField()
    name_en = forms.CharField()

    class Meta:
        model = StadiumModel
        exclude = ('name',)