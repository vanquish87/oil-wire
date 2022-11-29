# Generated by Django 4.1 on 2022-11-28 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanical', '0002_alter_electricalrunninghours_runninghours'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='electricalrunninghours',
            name='hours_0_24',
        ),
        migrations.AlterField(
            model_name='electricalrunninghours',
            name='runninghours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='electricalshift',
            name='runninghours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='electricalshift',
            name='totalcummulative',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
