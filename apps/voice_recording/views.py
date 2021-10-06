from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from .voice_recording import VoiceRecordingController
from rest_framework.permissions import AllowAny

recording_obj = VoiceRecordingController()


# Create your views here.

@permission_classes((AllowAny,))
class VoiceRecordingView(APIView):
    def get(self, request, recording_id=None):
        result = recording_obj.get_entity(request=request, recording_id=recording_id)
        return result

    def post(self, request):
        result = recording_obj.create_entity(request=request)
        return result

