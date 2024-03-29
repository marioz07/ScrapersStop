# Generated by Django 3.2.7 on 2022-04-17 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('Scrap', models.CharField(max_length=50)),
                ('Weight', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=300)),
                ('Address2', models.CharField(max_length=300)),
                ('locality', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
