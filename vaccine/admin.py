from django.contrib import admin

# Register your models here.

from .models import Vaccine, VaccineNeedy

admin.site.register(Vaccine)
admin.site.register(VaccineNeedy)
