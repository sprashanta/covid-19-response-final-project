from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone_number', 'email', 'nid_image', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        return user

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


class DonorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone_number', 'email', 'nid_image', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_donor = True
        user.save()
        return user

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


class DoctorUpdateForm(forms.ModelForm):
    specialist = forms.ModelMultipleChoiceField(
        queryset=Specialist.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    degree = forms.ModelMultipleChoiceField(
        queryset=Degree.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(DoctorUpdateForm, self).__init__(*args, **kwargs)
        for username in self.fields.keys():
            self.fields[username].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'specialist', 'degree', 'address', 'image', 'nid_image']


class PatientUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'address', 'image', 'nid_image']


class DonorUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'address', 'image', 'nid_image']
