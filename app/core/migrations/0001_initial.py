# Generated by Django 4.1.5 on 2023-01-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('serial_number', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
