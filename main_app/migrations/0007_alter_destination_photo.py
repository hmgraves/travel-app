# Generated by Django 4.0.3 on 2022-04-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_destination_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='photo',
            field=models.URLField(),
        ),
    ]