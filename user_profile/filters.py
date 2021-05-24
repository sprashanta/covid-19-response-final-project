import django_filters
from .models import Plasma, Hospital, Location
from django import forms


class HospitalLocationFilters(django_filters.FilterSet):
    # location = django_filters.ModelMultipleChoiceFilter(queryset=Location.objects.all(),
    #                                                     widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Hospital
        fields = ['location']


class PlasmaDonorFilters(django_filters.FilterSet):
    # donor_location = django_filters.ModelMultipleChoiceFilter(queryset=Location.objects.all(),
    #                                                     widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Plasma
        fields = ['blood_group', 'donor_location']
