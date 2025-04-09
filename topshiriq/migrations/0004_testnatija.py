# Generated by Django 5.1.6 on 2025-04-09 05:54

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0003_remove_topshiriq_test_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestNatija',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('togri_soni', models.IntegerField()),
                ('jami_soni', models.IntegerField()),
                ('foiz', models.FloatField()),
                ('topshiriq', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='natijalar', to='topshiriq.topshiriq')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
