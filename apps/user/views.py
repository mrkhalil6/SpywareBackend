from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .user import UserController, create_message
from rest_framework.permissions import AllowAny

user_obj = UserController()


# Create your views here.


class UserView(APIView):
    def get(self, request, user_id=None):
        result = user_obj.get_user(request=request, user_id=user_id)
        return result

    def patch(self, request, user_id=None):
        if user_id is None:
            return Response(create_message(True, 'query_param_missing', []))
        result = user_obj.update_user(request_body=request.data, user_id=user_id)
        return result

    def delete(self, request, user_id=None):
        if user_id is None:
            return Response(create_message(True, 'query_param_missing', []))
        result = user_obj.delete_user(user_id=user_id)
        return result


class UserLogoutView(APIView):
    def post(self, request):
        result = user_obj.user_logout(request_body=request.data)
        return result


class UserFilterView(APIView):
    def post(self, request):
        result = user_obj.filter_user(request=request)
        return result


@api_view(['POST'])
@permission_classes((AllowAny,))
def user_login(request):
    result = user_obj.user_login(request=request)
    print(result)
    return result


@api_view(['POST'])
# @permission_classes((AllowAny,))
def user_create(request):
    result = user_obj.create_user(request_body=request.data)
    return result
