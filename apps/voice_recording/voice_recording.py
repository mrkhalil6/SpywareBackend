from rest_framework.response import Response
from django.db import IntegrityError

from .models import VoiceRecording
from .serializer import *
from common.utils import create_message

type_obj = Types()


class VoiceRecordingController:
    def get_entity(self, request, recording_id):
        try:
            if recording_id is None:
                limit = 10
                page = int(request.GET.get("page", "1"))
                if page < 1:
                    return Response(create_message(True, 'invalid_page', []))
                device_id = request.device_id

                total_count = VoiceRecording.objects.all().count()
                skip_values = (page - 1) * limit
                offset = skip_values + limit
                print(device_id)

                entity_obj = VoiceRecording.objects.filter(device_id=device_id)[skip_values:offset]
                json_parse = GetVoiceRecordingSerializer(entity_obj, context={"request": request}, many=True)

                data_to_send = {
                    "total_count": total_count,
                    "recording_data": json_parse.data
                }
                return Response(create_message(False, "success", data_to_send))
            else:
                try:
                    device_id = request.device_id
                    pictures_obj = VoiceRecording.objects.get(id=recording_id, device_id=device_id)
                    json_parse = GetVoiceRecordingSerializer(pictures_obj, context={"request": request})
                    return Response(create_message(False, "success", [json_parse.data]))
                except VoiceRecording.DoesNotExist:
                    return Response(create_message(True, 'not_found', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def create_entity(self, request):
        try:
            request_body = request.data
            request_body["device"] = request.device_id
            entity_obj = VoiceRecordingSerializer(data=request_body)
            try:
                if entity_obj.is_valid():
                    entity_obj.save()
                    return Response(create_message(False, 'creation_success', []))
                print(entity_obj.errors)
                return Response(create_message(True, 'data_error_message', [entity_obj.errors]))
            except IntegrityError:
                return Response(create_message(True, 'unique_picture', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))
