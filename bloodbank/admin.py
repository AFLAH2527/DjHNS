from django.contrib import admin

# Register your models here.

from .models import BloodDonor, BloodGroup

admin.site.register(BloodDonor)
admin.site.register(BloodGroup)