# Generated by Django 5.1.6 on 2025-03-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='majburiytopshiriq',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ozsohasidatopshiriq',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ozxohishibilantopshiriq',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='qoshimchatopshiriq',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topshiriq',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
