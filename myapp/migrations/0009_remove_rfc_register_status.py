# Generated by Django 4.2.7 on 2024-05-01 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_rfc_register_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfc_register',
            name='status',
        ),
    ]
