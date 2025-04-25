#Imports externes
from django import forms

#imports internes
from intranet.models import Aeronef

#Aeronefs/paramètres
class gererAeronefForm(forms.ModelForm):
    class Meta:
        model = Aeronef
        fields = ('type',
                  'classeULM',
                  'tarifPilote',
                  'tarifElevePilote',
                  )
        labels = {'type'        : 'Type ULM ' ,
                  'classeULM'   : 'classe ULM ',
                  'tarifPilote' : 'Prix Location (€/min) ',
                  'tarifElevePilote' : 'Prix instruction (€/min) ',
                  'prout' : 'prout '
                  }
    
