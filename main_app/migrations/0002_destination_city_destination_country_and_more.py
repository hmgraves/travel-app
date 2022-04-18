# Generated by Django 4.0.3 on 2022-04-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='country',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='location_description',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='time_zone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
