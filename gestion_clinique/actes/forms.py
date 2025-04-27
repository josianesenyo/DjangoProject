import datetime
from django import forms
from .models import Acte

class ActeForm(forms.ModelForm):

    class Meta:
        model = Acte
        fields = ['nom', 'description', 'prix']
