from django.contrib import admin
from .models import *


admin.site.register(MakeAppointment)
admin.site.register(Vaccine)
admin.site.register(IcuBedBooking)
admin.site.register(OxygenCylinderBooking)
