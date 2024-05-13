# Generated by Django 5.0.2 on 2024-03-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_report_reviewer_comments_alter_user_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rolls',
            field=models.CharField(choices=[('Common', 'Common'), ('IFC JC Counselor', 'IFC JC Counselor'), ('Django Admin', 'Django Admin'), ('IFC JC Admin', 'IFC JC Admin'), ('Anonymous', 'Anonymous')], default='Common', max_length=20),
        ),
    ]