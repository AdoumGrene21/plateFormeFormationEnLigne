# Generated by Django 3.2.8 on 2021-11-11 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0003_forma_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forma',
            name='description',
        ),
    ]