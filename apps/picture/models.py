from django.db import models
from apps.devices.models import Devices
from common.models import Base


class Picture(Base):
    image_path = models.ImageField(upload_to='media/', default='media/no_image.png', null=True, blank=True)
    device = models.ForeignKey(Devices, blank=True, related_name="picture_device_fk",
                                    null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'pictures'
        verbose_name_plural = 'pictures'

    def __str__(self):
        try:
            return self.image_path
        except:
            return "Default Image"
