# Generated by Django 2.2.14 on 2022-04-26 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20220426_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='situation',
            new_name='Situation',
        ),
    ]
