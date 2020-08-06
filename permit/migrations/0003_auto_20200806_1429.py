# Generated by Django 3.1 on 2020-08-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permit', '0002_auto_20200806_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='HarvestingPermit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='transportpermit',
            name='category',
            field=models.CharField(choices=[('AM', 'Amakara'), ('AS', 'Amasiteri'), ('IM', 'Imbaho'), ('IB', 'Ibiti')], default='AM', max_length=2),
        ),
    ]