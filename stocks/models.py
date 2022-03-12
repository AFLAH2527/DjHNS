from django.db import models
from bloodbank.models import BloodGroup
from vaccine.models import Vaccine
# Create your models here.

class BloodStock(models.Model):
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.blood_group}({self.count})'

class VaccineStock(models.Model):
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.vaccine_name}({self.count})'

