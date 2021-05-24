from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User
from SuperAdmin.models import *


class User(AbstractUser):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, verbose_name='Hospital Name',
                                    null=True, blank=True)
    specialist = models.ManyToManyField(Specialist)
    degree = models.ManyToManyField(Degree)
    is_patient = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    nid_image = models.ImageField(upload_to='nid_pics', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
