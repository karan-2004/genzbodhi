# Generated by Django 4.2.5 on 2024-01-21 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_alter_post_postedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 21, 11, 15, 14, 44051)),
        ),
    ]
