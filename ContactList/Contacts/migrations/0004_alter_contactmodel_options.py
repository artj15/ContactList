# Generated by Django 3.2.3 on 2021-05-17 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0003_alter_contactmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'ordering': ['surname', 'name'], 'verbose_name': 'Contact'},
        ),
    ]
