# Generated by Django 3.2.8 on 2021-11-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0004_remove_forma_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forma',
            old_name='type',
            new_name='description',
        ),
    ]
