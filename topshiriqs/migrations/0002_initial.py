# Generated by Django 5.1.4 on 2025-01-31 05:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topshiriqs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='majburiytopshiriq',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qoshimchatopshiriq',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topshiriq',
            name='users',
            field=models.ManyToManyField(related_name='topshiriq', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qoshimchatopshiriq',
            name='topshiriq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topshiriqs.topshiriq'),
        ),
        migrations.AddField(
            model_name='majburiytopshiriq',
            name='topshiriq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topshiriqs.topshiriq'),
        ),
    ]
