from django.db import models

# Create your models here.

class BloodGroup(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class BloodDonor(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.SET_DEFAULT, null=True, default="covishield")
    
    def __str__(self):
        return self.name
