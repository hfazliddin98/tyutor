# Generated by Django 5.1.4 on 2024-12-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='parol',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
