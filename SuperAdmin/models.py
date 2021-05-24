from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
import datetime


class Location(models.Model):
    location_name = models.CharField('Location Name', max_length=130)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_name


class Hospital(models.Model):
    name = models.CharField('Hospital Name', max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Specialist(models.Model):
    name = models.CharField('Specialist', max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Degree(models.Model):
    degree = models.CharField('Degree', max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.degree


class IcuBed(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    icu_bed_number = models.IntegerField(verbose_name='Hospital ICU Bed Number')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital


class OxygenCylinder(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=150, verbose_name='Organization Name')
    organization_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital


class Plasma(models.Model):
    donor_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = (
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    blood_group = models.CharField(default=False, choices=group, max_length=4, verbose_name='Blood Group')
    donor_location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Donor Location')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.donor_name)

    def days_different(self):
        now_date = datetime.datetime.now(tz=pytz.timezone('Asia/Dhaka'))
        diff_timedelta = now_date - self.created
        if 90 > diff_timedelta.days:
            pass
        return {
            "day": diff_timedelta.days,
            "hour": int(diff_timedelta.seconds / 3600),
            "minute": int((diff_timedelta.seconds % 3600) / 60),
        }
