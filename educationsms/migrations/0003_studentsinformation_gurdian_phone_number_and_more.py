# Generated by Django 4.2 on 2025-02-04 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationsms', '0002_detailsofteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsinformation',
            name='gurdian_phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format '01XXXXXXXXX' and be exactly 11 digits long.", regex='^01\\d{9}$')]),
        ),
        migrations.AddField(
            model_name='studentsinformation',
            name='iam_gurdian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentsinformation',
            name='iam_student',
            field=models.BooleanField(default=False),
        ),
    ]
