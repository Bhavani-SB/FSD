# Generated by Django 5.1 on 2024-10-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20240930_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentdetail',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
