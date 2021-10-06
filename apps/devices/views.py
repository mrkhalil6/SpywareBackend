# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.devices.devices import DevicesController

devices_controller_obj = DevicesController()


@permission_classes((AllowAny,))
class DeviceView(APIView):
    def post(self, request):
        result = devices_controller_obj.create_devices_entry(request=request)
        return result

    def get(self, request):
        result = devices_controller_obj.get_devices(request=request)
        return result

    def patch(self, request, devices_id=None):
        result = devices_controller_obj.update_devices(request=request, devices_id=devices_id)
        return result

    def delete(self, request, devices_id=None):
        result = devices_controller_obj.delete_devices(request=request, devices_id=devices_id)
        return result
