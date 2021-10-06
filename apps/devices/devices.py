from rest_framework.response import Response

from apps.devices.serializer import *
from common.utils import create_message
from apps.devices.models import Devices


class DevicesController:

    def create_devices_entry(self, request):
        try:
            request_body = request.data

            device_name = request_body.get("device_name")
            device_model = request_body.get("device_model")
            os = request_body.get("os")
            # user = request.user
            data_for_serializer = {
                "device_name": device_name,
                "device_model": device_model,
                # "user": user,
                "os": os,
            }

            add_devices = DeviceSerializer(data=data_for_serializer)
            if add_devices.is_valid():
                print("inside is valid")
                add_devices.save()
                return Response(create_message(False, 'success', add_devices.data))

            else:
                print("inside invalid data ")
                return Response(create_message(True, 'invalid_data', [add_devices.errors]))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def get_devices(self, request):
        try:

            limit = 10
            page = int(request.GET.get("page", "1"))
            if page < 1:
                return Response(create_message(True, 'invalid_page', []))
            request_user = request.user.id
            total_count = Devices.objects.filter(status=2, user_id=request_user).count()
            skip_values = (page - 1) * limit
            offset = skip_values + limit
            devices_obj = Devices.objects.filter(status=2, user_id=request_user)[skip_values:offset]
            get_devices = GetDeviceSerializer(devices_obj, many=True, context=request)
            data_to_send = {
                "total_count": total_count,
                "devices_data": get_devices.data
            }
            return Response(create_message(False, 'success', data_to_send))

        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def delete_devices(self, request, devices_id=None):
        if devices_id:
            try:
                devices_obj = Devices.objects.get(id=devices_id)
                devices_obj.status = 4
                devices_obj.save()
                return Response(create_message(False, 'success', []))
            except Devices.DoesNotExist:
                print("Invalid ID ")
                return Response(create_message(True, 'invalid_ID', []))
        else:
            print("No ID specified")
            return Response(create_message(True, 'exception_message', []))

    def update_devices(self, request, devices_id=None):
        if devices_id:
            try:
                request_body = request.data
                device_name = request_body.get("device_name")
                device_model = request_body.get("device_model")
                os = request_body.get("os")

                data_for_serializer = {
                    "device_name": device_name,
                    "device_model": device_model,
                    "os": os
                }

                serialized_data = UpdateDeviceSerializer(data=data_for_serializer)
                if serialized_data.is_valid():
                    devices_obj = Devices.objects.get(pk=devices_id)
                    for key, value in serialized_data.validated_data.items():
                        setattr(devices_obj, key, value)
                    devices_obj.save()
                    return Response(create_message(False, 'success', []))
                else:
                    return Response(create_message(True, 'exception_message', [serialized_data.errors]))
            except Devices.DoesNotExist:
                print("Invalid ID ")
                return Response(create_message(True, 'invalid_ID', []))
        else:
            print("No ID specified")
            return Response(create_message(True, 'exception_message', []))
