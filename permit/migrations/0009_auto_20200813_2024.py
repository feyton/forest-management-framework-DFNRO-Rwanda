# Generated by Django 3.0.6 on 2020-08-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permit', '0008_delete_harvestingpermit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportvehicle',
            name='max_q',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ibyo itwara(Toni)'),
        ),
    ]
