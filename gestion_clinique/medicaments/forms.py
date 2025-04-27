from django import forms
from .models import Medicament
from datetime import date

class MedicamentForm(forms.ModelForm):
    date_expiration = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d'),
            }
        )
    )

    class Meta:
        model = Medicament
        fields = '__all__'
        