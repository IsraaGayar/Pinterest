# Generated by Django 3.2.9 on 2021-11-29 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pins', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[{'H', 'Heart'}, {'L', 'Like'}, {'J', 'Joyful'}, {'H', 'Haha'}], max_length=500)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('pin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pinlikes', to='pins.pin')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pins.pin')),
            ],
            options={
                'ordering': ('-creationDate',),
            },
        ),
    ]
