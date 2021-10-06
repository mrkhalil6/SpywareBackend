from django.db import models
from apps.devices.models import Devices
from common.models import Base


class VoiceRecording(Base):
    recording_file = models.FileField(upload_to='media/', null=False, blank=False)
    device = models.ForeignKey(Devices, blank=True, related_name="recording_device_fk",
                               null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'voice_recording'
        verbose_name_plural = 'voice_recordings'

    def __str__(self):
        try:
            return self.recording_file
        except:
            return "Default Recording"
