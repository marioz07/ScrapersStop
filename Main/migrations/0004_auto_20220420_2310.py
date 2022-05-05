# Generated by Django 3.2.7 on 2022-04-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_orders_scrap'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Scrap',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Scrap',
        ),
    ]