from django import forms
from .models import Patient
from datetime import date

class PatientForm(forms.ModelForm):

    date_naissance = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'max': date.today().strftime('%Y-%m-%d'),
            }
        )
    )
    
    sexe = forms.ChoiceField(
        choices=[('M', 'Masculin'), ('F', 'Féminin')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Patient
        fields = '__all__'
