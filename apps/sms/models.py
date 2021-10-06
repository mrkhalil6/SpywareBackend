from django.db import models

# Create your models here.
from common.models import Base
from apps.devices.models import Devices


class SMS(Base):
    id = models.AutoField(primary_key=True)
    sms_id = models.IntegerField(blank=True, null=True)
    threadId = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    person = models.IntegerField(blank=True, null=True)
    protocol = models.IntegerField(blank=True, null=True)
    locked = models.BooleanField(blank=True, null=True)
    read = models.BooleanField(blank=True, null=True)
    seen = models.BooleanField(blank=True, null=True)
    receivedDate = models.BigIntegerField(blank=True, null=True)
    sentDate = models.BigIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    device = models.ForeignKey(Devices, related_name='%(app_label)s_%(class)s_fk', null=True, blank=True,
                               on_delete=models.CASCADE)

    class Meta:
        db_table = 'sms'
        verbose_name_plural = 'sms'

