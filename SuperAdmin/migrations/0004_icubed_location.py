# Generated by Django 2.2.5 on 2021-05-01 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperAdmin', '0003_auto_20210501_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='icubed',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SuperAdmin.Location'),
            preserve_default=False,
        ),
    ]
