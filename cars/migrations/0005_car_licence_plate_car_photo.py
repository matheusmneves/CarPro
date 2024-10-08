# Generated by Django 5.1 on 2024-08-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='licence_plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
