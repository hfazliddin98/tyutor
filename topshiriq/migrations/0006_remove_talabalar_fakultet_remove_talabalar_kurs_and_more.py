# Generated by Django 5.1.6 on 2025-03-19 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0005_alter_majburiytopshiriq_tur_and_more'),
        ('users', '0004_fakultet_is_active_guruh_is_active_kurs_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talabalar',
            name='fakultet',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='kurs',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='yonalish',
        ),
        migrations.AddField(
            model_name='talabalar',
            name='sardor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='talabalar',
            name='guruh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.guruh'),
        ),
    ]
