from django.forms import ModelForm
from .models import BloodStock, VaccineStock

class BloodStockCreateForm(ModelForm):
    class Meta:
        model = BloodStock
        fields = (
            'blood_group',
        )

class VaccineStockCreateForm(ModelForm):
    class Meta:
        model = VaccineStock
        fields = (
            'vaccine_name',
        )

class BloodStockUpdateForm(ModelForm):
    class Meta:
        model = BloodStock
        fields = (
            'blood_group',
            'count'
        )

class VaccineStockUpdateForm(ModelForm):
    class Meta:
        model = VaccineStock
        fields = (
            'vaccine_name',
            'count'
        )

        