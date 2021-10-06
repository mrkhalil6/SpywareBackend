from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from .reporting import ReportingController
from rest_framework.permissions import AllowAny

reporting_obj = ReportingController()


# Create your views here.

@permission_classes((AllowAny,))
class ReportingView(APIView):
    def get(self, request):
        result = reporting_obj.get_entity(request=request)
        return result


