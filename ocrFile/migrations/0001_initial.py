# Generated by Django 4.1 on 2022-12-05 07:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, upload_to='ocr/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
            ],
        ),
    ]
