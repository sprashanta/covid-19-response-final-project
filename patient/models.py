from django.db import models
from django.conf import settings
from SuperAdmin.models import Hospital


class MakeAppointment(models.Model):
    approve = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Decline', 'Decline'),
    )
    doctor_checkup = (
        ('Checked', 'Checked'),
        ('Not Checked', 'Not Checked')
    )
    patient_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_name',
                                     verbose_name='Patient Name')
    patient_description = models.CharField(max_length=254, verbose_name='What Is Your Problem')
    doctor_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_name',
                                    null=True, blank=True, verbose_name='Doctor Name',
                                    limit_choices_to={'is_doctor': True})
    meet_link = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=approve, default='Pending', verbose_name='Appointment Status')
    date = models.DateField(null=True, blank=True)
    time = models.CharField(null=True, blank=True, max_length=10)
    doctor_checkup = models.CharField(max_length=15, choices=doctor_checkup, default='Not Checked',
                                      verbose_name='Doctor Check Up Status')

    def __str__(self):
        return self.patient_name


class Vaccine(models.Model):
    vaccine_approve = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Decline', 'Decline'),
    )
    patient_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                     related_name='vaccine_patient_name',
                                     verbose_name='Patient Name')
    hospital_name = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name',
                                         related_name='hospital')
    status = models.CharField(max_length=15, choices=vaccine_approve, default='Pending', verbose_name='Vaccine Status')
    nid_image = models.ImageField(upload_to='vaccine_nid_image', verbose_name='NID Image')
    first_dos = models.DateField(null=True, blank=True, verbose_name='Vaccine First Dos')
    second_dos = models.DateField(null=True, blank=True, verbose_name='Vaccine Second Dos')

    def __str__(self):
        return str(self.patient_name)


class IcuBedBooking(models.Model):
    icu_bed_booking_approve = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Decline', 'Decline'),
    )
    patient_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                     related_name='icu_bed_booking_patient_name',
                                     verbose_name='Patient Name')
    hospital_name = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name',
                                      related_name='icu_bed_booking_hospital_name')
    status = models.CharField(max_length=15, choices=icu_bed_booking_approve, default='Pending',
                              verbose_name='Icu Bed Booking Status')

    def __str__(self):
        return str(self.patient_name)


class OxygenCylinderBooking(models.Model):
    oxygen_cylinder_booking_approve = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Decline', 'Decline'),
    )
    patient_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                     related_name='oxygen_cylinder_booking_patient_name',
                                     verbose_name='Patient Name')
    hospital_name = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name',
                                      related_name='oxygen_cylinder_booking_hospital_name')
    status = models.CharField(max_length=15, choices=oxygen_cylinder_booking_approve, default='Pending',
                              verbose_name='Oxygen Cylinder Booking Status')

    def __str__(self):
        return str(self.patient_name)
