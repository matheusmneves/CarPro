# Generated by Django 5.1 on 2024-08-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
