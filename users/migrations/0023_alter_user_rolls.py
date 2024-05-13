# Generated by Django 4.2.11 on 2024-03-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_report_date_of_incident_alter_reportfile_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('Django Admin', 'Django Admin'), ('IFC JC Admin', 'IFC JC Admin'), ('Anonymous', 'Anonymous'), ('IFC JC Counselor', 'IFC JC Counselor'), ('Common', 'Common')], default='Common', max_length=20),
        ),
    ]