from rest_framework.response import Response
from django.db import IntegrityError

from apps.contacts.models import Contacts
from apps.picture.models import Picture
from apps.sms.models import SMS
from apps.voice_recording.models import VoiceRecording
from common.utils import create_message


class ReportingController:
    def get_entity(self, request):
        try:
            device_id = request.device_id
            contacts_count = Contacts.objects.filter(device_id=device_id).count()
            sms_count = SMS.objects.filter(device_id=device_id).count()
            pictures_count = Picture.objects.filter(device_id=device_id).count()
            voice_recording_count = VoiceRecording.objects.filter(device_id=device_id).count()
            data_to_send = {
                "contacts_count": contacts_count,
                "sms_count": sms_count,
                "pictures_count": pictures_count,
                "voice_recording_count": voice_recording_count,

            }
            return Response(create_message(False, "success", data_to_send))
        except Exception as ex:
            print(ex)
            return Response(create_message(True, 'exception', []))
