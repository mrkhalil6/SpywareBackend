from rest_framework.response import Response
from django.db import IntegrityError

from .serializer import *
from common.utils import create_message

type_obj = Types()


class PictureController:
    def get_entity(self, request, picture_id):
        try:
            if picture_id is None:
                limit = 12
                page = int(request.GET.get("page", "1"))
                if page < 1:
                    return Response(create_message(True, 'invalid_page', []))
                device_id = request.device_id

                total_count = Picture.objects.filter(device_id=device_id).count()
                skip_values = (page - 1) * limit
                offset = skip_values + limit
                print(device_id)

                pictures_obj = Picture.objects.filter(device_id=device_id)[skip_values:offset]
                json_parse = GetPictureSerializer(pictures_obj, context={"request": request}, many=True)

                data_to_send = {
                    "total_count": total_count,
                    "pictures_data": json_parse.data
                }
                return Response(create_message(False, "success", data_to_send))
            else:
                try:
                    device_id = request.device_id
                    pictures_obj = Picture.objects.get(id=picture_id, device_id=device_id)
                    json_parse = GetPictureSerializer(pictures_obj, context={"request": request})
                    return Response(create_message(False, "success", [json_parse.data]))
                except Picture.DoesNotExist:
                    return Response(create_message(True, 'not_found', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def create_entity(self, request):
        try:
            request_body = request.data
            request_body["device"] = request.device_id
            entity_obj = PictureSerializer(data=request_body)
            try:
                if entity_obj.is_valid():
                    entity_obj.save()
                    return Response(create_message(False, 'creation_success', []))
                print(entity_obj.errors)
                return Response(create_message(True, 'data_error_message', [entity_obj.errors]))
            except IntegrityError:
                return Response(create_message(True, 'unique_email', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))
