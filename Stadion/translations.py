from modeltranslation.translator import translator, TranslationOptions
from bron.models import StadiumModel , BronModel


class StadiumTranslationOptions(TranslationOptions):
    fields = ('name', 'address',)
    required_languages = ('uz', )

class BronTranslationOptions(TranslationOptions):
    fields = ('stadium',)
    required_languages = ('uz',)

translator.register(BronModel, StadiumModel, StadiumTranslationOptions, BronTranslationOptions)