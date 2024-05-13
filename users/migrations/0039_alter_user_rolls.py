# Generated by Django 5.0.3 on 2024-04-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_alter_user_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('IFC JC Admin', 'IFC JC Admin'), ('Common', 'Common'), ('IFC JC Counselor', 'IFC JC Counselor'), ('Django Admin', 'Django Admin'), ('Anonymous', 'Anonymous')], default='Common', max_length=20),
        ),
    ]