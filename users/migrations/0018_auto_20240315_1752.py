# Generated by Django 5.0.2 on 2024-03-15 22:52

from django.db import migrations

def add_standard_of_conducts(apps, schema_editor):
    StandardOfConduct = apps.get_model('users', 'StandardOfConduct')

    for i in range(1, 15):
        standard, created = StandardOfConduct.objects.get_or_create(standard=i)
        if created:
            print(f"StandardOfConduct {i} created.")
        else:
            print(f"StandardOfConduct {i} already exists.")

def remove_standard_of_conducts(apps, schema_editor):
    StandardOfConduct = apps.get_model('users', 'StandardOfConduct')

    for i in range(1, 15):
        standard = StandardOfConduct.objects.get(standard=i)
        standard.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_standardofconduct_standard_alter_user_rolls'),
    ]

    operations = [
        migrations.RunPython(add_standard_of_conducts, remove_standard_of_conducts)
    ]