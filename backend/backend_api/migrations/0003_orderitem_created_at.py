# Generated by Django 3.2.23 on 2024-02-08 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_auto_20240208_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
