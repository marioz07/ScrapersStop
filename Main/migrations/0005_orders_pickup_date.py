# Generated by Django 3.2.7 on 2022-04-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20220420_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Pickup_date',
            field=models.DateField(null=True, verbose_name='Pickup date'),
        ),
    ]
