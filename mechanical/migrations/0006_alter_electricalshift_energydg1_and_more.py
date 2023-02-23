# Generated by Django 4.1 on 2023-02-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mechanical", "0005_alter_electricalshift_energydg1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg1",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg2",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg3",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="electricalshift",
            name="energydg4",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
    ]
