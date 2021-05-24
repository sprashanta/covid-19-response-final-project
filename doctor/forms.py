from django import forms
from patient.models import *


class DoctorChangeCheckUpForm(forms.ModelForm):
    class Meta:
        model = MakeAppointment
        fields = ['doctor_checkup']
