from django import forms
from .models import VaccineNeedy

class VaccineRegForm(forms.ModelForm):
    class Meta:
        model = VaccineNeedy
        fields = ['name', 'email', 'age', 'place', 'refid', 'needed_vaccine']