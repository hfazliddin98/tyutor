# Generated by Django 5.1.4 on 2025-02-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0015_ozsohasidatopshiriq_ozxohishibilantopshiriq'),
    ]

    operations = [
        migrations.AddField(
            model_name='topshiriq',
            name='test_file',
            field=models.FileField(blank=True, null=True, upload_to='topshiriq/topshiriq/test'),
        ),
    ]
