# Generated by Django 4.0.6 on 2022-07-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanical', '0002_rig'),
    ]

    operations = [
        migrations.AddField(
            model_name='rig',
            name='slug',
            field=models.CharField(default=0, max_length=255, unique=True),
        ),
    ]
