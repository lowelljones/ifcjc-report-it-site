# Generated by Django 4.2.11 on 2024-03-17 06:19

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_merge_20240317_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_of_incident',
            field=models.DateField(validators=[users.models.Report.validate_date_of_incident]),
        ),
        migrations.AlterField(
            model_name='reportfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('Common', 'Common'), ('IFC JC Admin', 'IFC JC Admin'), ('Django Admin', 'Django Admin'), ('IFC JC Counselor', 'IFC JC Counselor'), ('Anonymous', 'Anonymous')], default='Common', max_length=20),
        ),
    ]
