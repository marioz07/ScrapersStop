# Generated by Django 3.2.7 on 2022-04-20 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_scrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Scrap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.scrap'),
        ),
    ]