# Generated by Django 3.2.9 on 2021-11-27 00:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211126_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follow',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
