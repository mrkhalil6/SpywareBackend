from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from common.enum import Types
from .models import Picture

type_obj = Types()


class GetPictureSerializer(ModelSerializer):
    image_path = SerializerMethodField('get_image_path', required=False)

    def get_image_path(self, obj):
        try:
            photo_url = obj.image_path.url
            return self.context['request'].build_absolute_uri(photo_url)
        except Exception as e:
            # print(e)
            return None

    class Meta:
        model = Picture
        fields = "__all__"


class PictureSerializer(ModelSerializer):

    class Meta:
        model = Picture
        fields = "__all__"

