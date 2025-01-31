# Generated by Django 5.1.4 on 2025-01-31 05:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MajburiyTopshiriq',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('tur', models.CharField(choices=[('ttjga_tashrif', 'ttjga_tashrif'), ('ijaraga_tashrif', 'ijaraga_tashrif'), ('tutorlik_soati', 'tutorlik_soati'), ('davra_suhbati', 'davra_suhbati'), ('tadbir', 'tadbir'), ('ttjda_tadbir', 'ttjda_tadbir'), ('iqtidorli_talabam', 'iqtidorli_talabam'), ('oilaga_xat', 'oilaga_xat')], max_length=30)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('body', models.TextField()),
                ('file1', models.FileField(upload_to='topshiriq/majburiy')),
                ('file2', models.FileField(upload_to='topshiriq/majburiy')),
                ('file3', models.FileField(upload_to='topshiriq/majburiy')),
                ('file4', models.FileField(upload_to='topshiriq/majburiy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QoshimchaTopshiriq',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('tur', models.CharField(choices=[('ttjga_tashrif', 'ttjga_tashrif'), ('ijaraga_tashrif', 'ijaraga_tashrif'), ('tutorlik_soati', 'tutorlik_soati'), ('davra_suhbati', 'davra_suhbati'), ('tadbir', 'tadbir'), ('ttjda_tadbir', 'ttjda_tadbir'), ('iqtidorli_talabam', 'iqtidorli_talabam'), ('oilaga_xat', 'oilaga_xat')], max_length=30)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('body', models.TextField()),
                ('file1', models.FileField(upload_to='topshiriq/qoshimcha')),
                ('file2', models.FileField(upload_to='topshiriq/qoshimcha')),
                ('file3', models.FileField(upload_to='topshiriq/qoshimcha')),
                ('file4', models.FileField(upload_to='topshiriq/qoshimcha')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topshiriq',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('topshiriq_turi', models.CharField(choices=[('majburiy', 'majburiy'), ('qoshimcha', 'qoshimcha')], max_length=30)),
                ('urinishlar_soni', models.CharField(blank=True, max_length=2)),
                ('boshlanish_vaqti', models.DateField()),
                ('tugash_vaqti', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
