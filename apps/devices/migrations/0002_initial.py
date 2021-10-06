# Generated by Django 3.2.7 on 2021-09-24 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='devices_devices_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='devices',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='devices_devices_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='devices',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='device_user_fk', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deviceapikey',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_api_keys', to='devices.devices'),
        ),
    ]
