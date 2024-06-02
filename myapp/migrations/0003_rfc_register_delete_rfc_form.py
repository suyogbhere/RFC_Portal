# Generated by Django 4.2.7 on 2024-04-27 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_authorizer_name_name_alter_executor_name_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RFC_Register',
            fields=[
                ('Rfc_Number', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('Reference_RFC_No', models.IntegerField(default=0)),
                ('Environment', models.CharField(max_length=100)),
                ('Planned_Date', models.DateField()),
                ('Reason_for_change', models.CharField(max_length=200)),
                ('Description_of_change', models.CharField(max_length=500)),
                ('Change_Requested_by', models.CharField(max_length=100)),
                ('Change_level', models.CharField(max_length=100)),
                ('Change_impact_assessment', models.CharField(max_length=200)),
                ('Risk_Rating', models.CharField(max_length=100)),
                ('Attachments', models.FileField(upload_to='Attachment')),
                ('Change_rollback_procedures', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('HOLD', 'HOLD'), ('CANCELLED', 'CANCELLED'), ('ROLLBACK', 'ROLLBACK'), ('CLOSED', 'CLOSED')], max_length=100, null=True)),
                ('Activity_Notes', models.CharField(blank=True, max_length=200, null=True)),
                ('Activity_Date', models.DateTimeField(null=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('Change_authorizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.authorizer_name')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
                ('Request_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.request_type')),
                ('System_Details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.system_details')),
                ('To_be_executed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.executor_name')),
            ],
        ),
        migrations.DeleteModel(
            name='RFC_Form',
        ),
    ]
