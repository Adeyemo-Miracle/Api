# Generated by Django 4.1.2 on 2022-10-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='completed',
            field=models.BooleanField(default=True),
        ),
    ]
