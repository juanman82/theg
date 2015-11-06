from haystack import indexes
from models import Perfil_Hombre
from models import Perfil_Mujer
from models import Perfil_Nino
from models import Perfil_Nina
 
class PerfilHombreIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.CharField()

    def get_model(self):
        return Perfil_Hombre

class PerfilMujerIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.CharField()

    def get_model(self):
        return Perfil_Mujer

class PerfilNinoIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.CharField()

    def get_model(self):
        return Perfil_Nino

class PerfilNinaIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.CharField()

    def get_model(self):
        return Perfil_Nina