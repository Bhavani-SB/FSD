# Generated by Django 5.1 on 2024-09-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_userdata_options_alter_userdata_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
