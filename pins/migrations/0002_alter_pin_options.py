# Generated by Django 3.2.9 on 2021-11-28 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pin',
            options={'ordering': ('-createdat',)},
        ),
    ]
