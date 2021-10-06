from rest_framework.response import Response

from apps.contacts.serializer import *
from apps.sms.models import SMS
from apps.sms.serializer import SMSSerializer
from common.utils import create_message
from apps.devices.models import Devices


class SMSController:

    def create_entity(self, request):
        print(request.data)
        try:
            device_id = request.device_id
            request_data = request.data
            for data in request_data:
                # check if a message already exists
                entity = SMS.objects.filter(device_id=device_id, sms_id=data.get("id")).first()
                if entity:
                    print("message already present in database")
                    pass
                else:
                    data["sms_id"] = data.get("id")
                    data["device"] = device_id
                    data.pop("id")
                    entity_serializer = SMSSerializer(data=data)
                    if entity_serializer.is_valid():
                        entity_serializer.save()
                    else:
                        print(entity_serializer.errors)
                        # return Response(create_message(True, 'invalid_data', [entity_serializer.errors]))
            return Response(create_message(False, 'success', []))
        except Exception as ex:
            print(ex)
            return Response(create_message(True, 'exception_message', []))

        # try:
        #     contacts_list = []
        #     for contact in request.data:
        #         contact["device_id"] = request.device_id
        #         contacts_list.append(contact)
        #
        #     add_contacts = ContactsSerializer(data=contacts_list, many=True)
        #     if add_contacts.is_valid():
        #         print("inside is valid")
        #         add_contacts.save()
        #         return Response(create_message(False, 'success', add_contacts.data))
        #
        #     else:
        #         print("inside invalid data ")
        #         return Response(create_message(True, 'invalid_data', [add_contacts.errors]))
        # except Exception as e:
        #     print(e)
        #     return Response(create_message(True, 'exception_message', []))

    def get_entity(self, request):
        try:
            limit = 10
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


class ConversationController:

    def get_entity(self, request):
        try:
            requested_device = request.device_id
            entity = SMS.objects.filter(device_id=requested_device).values('address').distinct()
            entity_serializer = SMSSerializer(entity, many=True)
            return Response(create_message(False, 'success', entity_serializer.data))

        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))


class ChatController:

    def get_entity(self, request, address=None):
        try:
            if address:
                requested_device = request.device_id
                entity = SMS.objects.filter(device_id=requested_device, address=address).order_by("created_datetime")
                entity_serializer = SMSSerializer(entity, many=True)
                return Response(create_message(False, 'success', entity_serializer.data))
            else:
                return Response(create_message(True, 'invalid_data', []))


        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))
