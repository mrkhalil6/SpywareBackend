from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from .models import Devices, Contacts
from common.enum import Types

type_obj = Types()


class ContactsSerializer(ModelSerializer):
    name = CharField(max_length=150, required=True, allow_null=False)
    phone_number = CharField(max_length=150, required=True, allow_null=False)
    # os = CharField(max_length=150, required=False, allow_null=False)
    device_id = IntegerField(required=True, allow_null=False)

    # def validate_os(self, value):
    #     print(self.context['request'], value)
    #     return self.context['request'].os
    #
    # def validate_device_id(self, value):
    #     return self.context['request'].device_id

    class Meta:
        model = Contacts
        fields = "__all__"


class GetContactSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

#
# class UpdateDeviceSerializer(ModelSerializer):
#
#     class Meta:
#         model = Devices
#         fields = "__all__"
