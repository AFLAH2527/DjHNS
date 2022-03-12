from django.contrib import admin

# Register your models here.

from .models import BloodStock, VaccineStock

admin.site.register(BloodStock)
admin.site.register(VaccineStock)