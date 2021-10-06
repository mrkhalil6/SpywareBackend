from django.db import models

# Create your models here.
from django.db.models import Q
from rest_framework_api_key.models import AbstractAPIKey, BaseAPIKeyManager

from SpywareBackendServer.settings import AUTH_USER_MODEL
from common.methods import create_device_key
from common.models import Base


class Devices(Base):
    id = models.AutoField(primary_key=True)
    device_name = models.TextField(blank=True, null=True)
    device_model = models.TextField(blank=True, null=True)
    os = models.TextField(blank=False, null=False)
    device_key = models.TextField(default=create_device_key)
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='device_user_fk', null=True, blank=True,
                             on_delete=models.PROTECT)

    class Meta:
        db_table = 'devices'
        verbose_name_plural = 'devices'


class DeviceAPIKey(AbstractAPIKey):
    device = models.ForeignKey(
        Devices,
        on_delete=models.CASCADE,
        related_name="device_api_keys",
    )


class DeviceAPIKeyManager(BaseAPIKeyManager):
    def get_usable_keys(self):
        return super().get_usable_keys().filter(~Q(status=4))
