from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from .models import Devices
from common.enum import Types

type_obj = Types()


class DeviceSerializer(ModelSerializer):
    device_name = CharField(max_length=150, required=True, allow_null=False)
    device_model = CharField(max_length=150, required=True, allow_null=False)
    os = CharField(max_length=150, required=True, allow_null=False)

    class Meta:
        model = Devices
        fields = "__all__"


class GetDeviceSerializer(ModelSerializer):
    class Meta:
        model = Devices
        fields = "__all__"


class UpdateDeviceSerializer(ModelSerializer):

    class Meta:
        model = Devices
        fields = "__all__"
