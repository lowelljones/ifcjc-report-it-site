# Generated by Django 5.0.2 on 2024-04-12 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_alter_user_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('IFC JC Counselor', 'IFC JC Counselor'), ('Anonymous', 'Anonymous'), ('IFC JC Admin', 'IFC JC Admin'), ('Django Admin', 'Django Admin'), ('Common', 'Common')], default='Common', max_length=20),
        ),
    ]