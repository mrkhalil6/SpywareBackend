from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .picture import PictureController, create_message
from rest_framework.permissions import AllowAny

picture_obj = PictureController()


# Create your views here.

@permission_classes((AllowAny,))
class PictureView(APIView):
    def get(self, request, picture_id=None):
        result = picture_obj.get_entity(request=request, picture_id=picture_id)
        return result

    def post(self, request):
        result = picture_obj.create_entity(request=request)
        return result

