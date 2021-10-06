from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .sms import SMSController, ConversationController, ChatController

sms_controller_obj = SMSController()
conversation_controller_obj = ConversationController()
chat_controller_obj = ChatController()


@permission_classes((AllowAny,))
class SMSView(APIView):
    def post(self, request):
        result = sms_controller_obj.create_entity(request=request)
        return result

    def get(self, request):
        result = sms_controller_obj.get_entity(request=request)
        return result

    # def patch(self, request, devices_id=None):
    #     result = sms_controller_obj.update_contacts(request=request, devices_id=devices_id)
    #     return result
    #
    # def delete(self, request, devices_id=None):
    #     result = sms_controller_obj.delete_contacts(request=request, devices_id=devices_id)
    #     return result


@permission_classes((AllowAny,))
class ConversationView(APIView):

    def get(self, request):
        result = conversation_controller_obj.get_entity(request=request)
        return result


@permission_classes((AllowAny,))
class ChatView(APIView):

    def get(self, request, address=None):
        result = chat_controller_obj.get_entity(request=request, address=address)
        return result

    # def patch(self, request, devices_id=None):
    #     result = sms_controller_obj.update_contacts(request=request, devices_id=devices_id)
    #     return result
    #
    # def delete(self, request, devices_id=None):
    #     result = sms_controller_obj.delete_contacts(request=request, devices_id=devices_id)
    #     return result
