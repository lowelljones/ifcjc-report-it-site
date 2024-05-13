# Generated by Django 4.2.11 on 2024-03-18 19:41

from django.db import migrations, models
import storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_user_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfile',
            name='file',
            field=models.FileField(blank=True, null=True, storage=storage_backends.MediaStorage(), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('Common', 'Common'), ('IFC JC Counselor', 'IFC JC Counselor'), ('IFC JC Admin', 'IFC JC Admin'), ('Django Admin', 'Django Admin'), ('Anonymous', 'Anonymous')], default='Common', max_length=20),
        ),
    ]
