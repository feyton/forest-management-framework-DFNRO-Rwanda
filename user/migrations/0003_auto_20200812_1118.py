# Generated by Django 3.0.6 on 2020-08-12 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permit', '0007_auto_20200812_1012'),
        ('user', '0002_auto_20200806_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cell',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='permit.Cell'),
        ),
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='permit.District'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='permit.Sector'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_dfnro',
            field=models.BooleanField(default=False),
        ),
    ]