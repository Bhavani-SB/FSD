# Generated by Django 5.1 on 2024-09-30 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_appointmentdetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='doc_img',
        ),
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='doc_name',
        ),
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='doc_spec',
        ),
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='user',
        ),
    ]
