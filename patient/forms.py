from django import forms
from .models import *


class MakeAppointmentForm(forms.ModelForm):
    class Meta:
        model = MakeAppointment
        fields = ['patient_description']


class PatientVaccineApply(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['hospital_name', 'nid_image']

