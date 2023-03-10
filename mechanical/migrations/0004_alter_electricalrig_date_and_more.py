# Generated by Django 4.1 on 2023-02-07 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mechanical", "0003_alter_electricalrig_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="electricalrig",
            name="date",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, null=True
            ),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg1",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg2",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg3",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg4",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
