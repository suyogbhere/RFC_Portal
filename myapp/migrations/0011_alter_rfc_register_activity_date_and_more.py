# Generated by Django 4.2.7 on 2024-05-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rfc_register_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfc_register',
            name='Activity_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rfc_register',
            name='Activity_Notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rfc_register',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
