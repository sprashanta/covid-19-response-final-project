from django import forms
from .models import *
from patient.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class SpecialistForm(forms.ModelForm):
    class Meta:
        model = Specialist
        fields = ['name']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_name']


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ['degree']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['location', 'name']


class DoctorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'hospital', 'email', 'phone_number', 'password1', 'password2']

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'), required=True)
    phone_number = forms.CharField(label=_('Phone Number'), help_text=_('Required. Enter an existing Email Number .'
                                                                        'plz enter 01...'),
                                   required=True)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        user = User.objects.filter(phone_number__iexact=phone_number).exists()
        if user:
            raise ValidationError(_('You can not use this Phone Number.'))

        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for username in self.fields.keys():
            self.fields[username].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'address', 'image']


class IcuBedForm(forms.ModelForm):
    class Meta:
        model = IcuBed
        fields = ['hospital', 'location', 'icu_bed_number']


class OxygenCylinderForm(forms.ModelForm):
    class Meta:
        model = OxygenCylinder
        fields = ['location', 'organization_name', 'organization_url']


class IcuBedUpdateForm(forms.ModelForm):
    class Meta:
        model = IcuBed
        fields = ['icu_bed_number']


class PlasmaForm(forms.ModelForm):
    class Meta:
        model = Plasma
        fields = ['blood_group', 'donor_location']


class UpdateMakeAppointmentForm(forms.ModelForm):
    patient_description = forms.CharField(disabled=True)
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.CharField(help_text='plz enter 10 am or 10 pm or 10A.M OR 10P.M')

    class Meta:
        model = MakeAppointment
        fields = ['patient_description', 'doctor_name', 'meet_link', 'status', 'date', 'time']


class UpdatePatientVaccine(forms.ModelForm):
    first_dos = forms.DateField(widget=forms.SelectDateWidget)
    second_dos = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Vaccine
        fields = ['status', 'first_dos', 'second_dos']


class IcuBedBookingStatusChange(forms.ModelForm):
    # hospital_name = forms.CharField(disabled=True)

    class Meta:
        model = IcuBedBooking
        fields = ['status']


class OxygenCylinderBookingStatusChange(forms.ModelForm):
    hospital_name = forms.CharField(disabled=True)

    class Meta:
        model = OxygenCylinderBooking
        fields = ['hospital_name', 'status']
