from rest_framework.response import Response

from apps.contacts.serializer import *
from common.utils import create_message
from apps.devices.models import Devices


class ContactsController:

    def create_contacts_entry(self, request):
        try:

            print(request.data)
            for contact in request.data:
                entity = Contacts.objects.filter(device_id=request.device_id,
                                                 phone_number=contact.get("phone_number")).first()
                if entity:
                    pass
                else:
                    contact["device_id"] = request.device_id
                    entity_serializer = ContactsSerializer(data=contact)
                    if entity_serializer.is_valid():
                        print("inside is valid")
                        entity_serializer.save()
            return Response(create_message(False, 'success', []))

        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def get_contacts(self, request):
        try:
            limit = 12
            page = int(request.GET.get("page", "1"))
            if page < 1:
                return Response(create_message(True, 'invalid_page', []))
            requested_device = request.device_id
            print(requested_device)
            total_count = Contacts.objects.filter(status=2, device_id=requested_device).count()
            skip_values = (page - 1) * limit
            offset = skip_values + limit
            contacts_obj = Contacts.objects.filter(status=2, device_id=requested_device)[skip_values:offset]
            get_contacts = GetContactSerializer(contacts_obj, many=True, context=request)
            data_to_send = {
                "total_count": total_count,
                "contacts_data": get_contacts.data
            }
            return Response(create_message(False, 'success', data_to_send))

        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def delete_contacts(self, request, contacts_id=None):
        if contacts_id:
            try:
                contacts_obj = contacts.objects.get(id=contacts_id)
                contacts_obj.status = 4
                contacts_obj.save()
                return Response(create_message(False, 'success', []))
            except contacts.DoesNotExist:
                print("Invalid ID ")
                return Response(create_message(True, 'invalid_ID', []))
        else:
            print("No ID specified")
            return Response(create_message(True, 'exception_message', []))

    def update_contacts(self, request, contacts_id=None):
        if contacts_id:
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

                serialized_data = Updatecontactserializer(data=data_for_serializer)
                if serialized_data.is_valid():
                    contacts_obj = contacts.objects.get(pk=contacts_id)
                    for key, value in serialized_data.validated_data.items():
                        setattr(contacts_obj, key, value)
                    contacts_obj.save()
                    return Response(create_message(False, 'success', []))
                else:
                    return Response(create_message(True, 'exception_message', [serialized_data.errors]))
            except contacts.DoesNotExist:
                print("Invalid ID ")
                return Response(create_message(True, 'invalid_ID', []))
        else:
            print("No ID specified")
            return Response(create_message(True, 'exception_message', []))
