from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from .models import SMS

from common.enum import Types

type_obj = Types()


class SMSSerializer(ModelSerializer):

    class Meta:
        model = SMS
        fields = "__all__"


class GetSMSSerializer(ModelSerializer):
    class Meta:
        model = SMS
        fields = "__all__"

