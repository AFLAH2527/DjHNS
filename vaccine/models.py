import email
from django.db import models

# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class VaccineNeedy(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    reg_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    refid = models.BigIntegerField()
    needed_vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_DEFAULT, null=True, default="covishield")
    is_mailed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
