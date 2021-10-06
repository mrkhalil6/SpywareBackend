from django.utils.deprecation import MiddlewareMixin

# from apps.vulnerability_management.models import Organization, Branch
from common.utils import create_message
from django.http import JsonResponse

from apps.devices.models import Devices


class DeviceKeyAUTH(MiddlewareMixin):
    device_id = ""

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        try:
            allowed_urls = ["/device/", "/admin/", "/user/", "/media/"]
            # if request.path.startswith('/admin/') or request.path.startswith('/core/user/'):
            # print(request.path)
            if request.path.startswith(tuple(allowed_urls)):
                return self.get_response(request)
            device_key = request.headers['X-Api-Key']
            print("DEVICE KEY: ", device_key)


            try:
                result = Devices.objects.get(device_key=device_key)
                print("DEVICE ID: ", result.id)
            except Devices.DoesNotExist:
                print("Device Does Not Exist !")
                return JsonResponse(create_message(True, "Device Does Not Exist !", []))

            # if not hasattr(request, "Devices_id") :
            setattr(request, "device", result)
            setattr(request, "device_id", result.id)
            setattr(request, "os", result.os)
            self.devices_id = result.id
            # print("Devices ID: ", self.Devices_id, ", Branch ID: ", self.branch_id)

            if result:
                pass
            else:
                print("Invalid Device-Key")
                return JsonResponse(create_message(True, "Invalid Keys!", []))
        except Exception as exx:
            print("Exception: ", exx)
            return JsonResponse(create_message(True, "exception", []))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def get_device_id(self):
        return self.devices_id
