from django import forms
from .models import BloodDonor

class DonorRegForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = ['name', 'email', 'age', 'place', 'blood_group']