from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .contacts import ContactsController

contacts_controller_obj = ContactsController()


@permission_classes((AllowAny,))
class ContactsView(APIView):
    def post(self, request):
        result = contacts_controller_obj.create_contacts_entry(request=request)
        return result

    def get(self, request):
        result = contacts_controller_obj.get_contacts(request=request)
        return result

    # def patch(self, request, devices_id=None):
    #     result = contacts_controller_obj.update_contacts(request=request, devices_id=devices_id)
    #     return result
    #
    # def delete(self, request, devices_id=None):
    #     result = contacts_controller_obj.delete_contacts(request=request, devices_id=devices_id)
    #     return result
