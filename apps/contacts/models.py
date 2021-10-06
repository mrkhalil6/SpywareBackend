from django.db import models

# Create your models here.
from common.models import Base
from apps.devices.models import Devices


class Contacts(Base):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    device = models.ForeignKey(Devices, related_name='%(app_label)s_%(class)s_fk', null=True, blank=True,
                               on_delete=models.CASCADE)

    class Meta:
        db_table = 'contacts'
        verbose_name_plural = 'contacts'

