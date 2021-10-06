from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db.models import Q
from django.db import IntegrityError
import json

from .serializer import *
from common.utils import create_message
import datetime
from common.methods import random_key_generator

type_obj = Types()


class UserController:
    def get_user(self, request, user_id):
        try:
            if user_id is None:
                # print(Headers({"":""}).get("branch_key"))
                user_list = User.objects.filter(~Q(status=4))
                json_parse = GetUserSerializer(user_list, context={"request": request}, many=True)
                return Response(create_message(False, "success", json_parse.data))
            else:
                try:
                    user = User.objects.get(~Q(status=4), id=user_id)
                    json_parse = GetUserSerializer(user, context={"request": request})
                    return Response(create_message(False, "success", [json_parse.data]))
                except User.DoesNotExist:
                    return Response(create_message(True, 'not_found', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def create_user(self, request_body):
        try:
            # request_body._mutable = True
            request_body['unique_code'] = random_key_generator(8)
            request_body['username'] = request_body.get('email')
            # request_body['verification_pin'] = secrets_obj.get_verification_pin()
            # request_body._mutable = False

            add_user = UserSerializer(data=request_body)
            print("Above try method")
            try:
                if add_user.is_valid():
                    add_user.save()
                    return Response(create_message(False, 'creation_success', []))
                print(add_user.errors)
                return Response(create_message(True, 'data_error_message', [add_user.errors]))
            except IntegrityError:
                return Response(create_message(True, 'unique_email', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def update_user(self, request_body, user_id):
        try:
            request_body._mutable = True
            request_body['modified_datetime'] = datetime.datetime.now()
            request_body._mutable = False
            update_user = UpdateUserSerializer(data=request_body)
            if update_user.is_valid():
                try:
                    user = User.objects.get(~Q(status=4), id=user_id)
                    for key, value in update_user.validated_data.items():
                        setattr(user, key, value)
                    user.save()
                    return Response(create_message(False, 'update_success', []))
                except User.DoesNotExist:
                    return Response(create_message(True, 'not_found', []))
            return Response(create_message(True, 'data_error_message', update_user.errors))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def delete_user(self, user_id):
        try:
            try:
                user = User.objects.get(~Q(status=4), id=user_id)
                user.status = 4
                user.save()
                return Response(create_message(False, 'success', []))
            except User.DoesNotExist:
                return Response(create_message(True, 'not_found', []))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def user_login(self, request):
        try:
            print(request.data)
            login_user = LoginSerializer(data=request.data)
            # print(login_user.initial_data)
            if login_user.is_valid():
                # print("Valid DATA")
                user = authenticate(username=login_user.data.get('username'), password=login_user.data.get('password'))
                # print(user)
                if user and user.status != 4:
                    token, created = Token.objects.get_or_create(user=user)
                    json_parse = GetUserSerializer(user, context={"request": request})
                    data = json_parse.data
                    data["token"] = token.key
                    user.last_login = datetime.datetime.now()
                    user.is_logged_in = True
                    user.save()
                    data["organization_key"] = user.organization.org_key
                    data["branch_key"] = user.branch.branch_key
                    return Response(create_message(False, 'login_successful', [data]))
                return Response(create_message(True, 'invalid_credentials', []))
            return Response(create_message(True, 'data_error_message', [login_user.errors]))
        except Exception as e:
            print("THIS IS THE EXCEPTION:", e)
            return Response(create_message(True, 'exception_message', []))

    def user_logout(self, request_body):
        try:

            try:
                user = User.objects.get(~Q(status=4), id=request_body.get('user_id'))
                Token.objects.filter(user=user).delete()
                return Response(create_message(False, 'success', []))
            except User.DoesNotExist:
                return Response(create_message(True, 'not_found', []))

        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))

    def filter_user(self, request):
        try:
            filter_data = FilterUserSerializer(data=request.data)

            if filter_data.is_valid():
                if filter_data.validated_data:
                    user_list = User.objects.filter(~Q(status=4), **filter_data.validated_data)
                    json_parse = GetUserSerializer(user_list, context={"request": request}, many=True)
                    return Response(create_message(False, 'success', json_parse.data))
                return Response(create_message(False, 'success', []))
            return Response(create_message(True, 'data_error_message', [filter_data.errors]))
        except Exception as e:
            print(e)
            return Response(create_message(True, 'exception_message', []))
