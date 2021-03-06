# Generated by Django 2.2.5 on 2021-05-01 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SuperAdmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='plasma',
            name='donor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oxygencylinder',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SuperAdmin.Location'),
        ),
        migrations.AddField(
            model_name='icubed',
            name='hospital',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SuperAdmin.Hospital', verbose_name='Hospital Name'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SuperAdmin.Location'),
        ),
    ]
