from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from common.enum import Types
from .models import VoiceRecording

type_obj = Types()


class GetVoiceRecordingSerializer(ModelSerializer):
    recording_file = SerializerMethodField('get_recording_file', required=False)

    def get_recording_file(self, obj):
        try:
            photo_url = obj.recording_file.url
            return self.context['request'].build_absolute_uri(photo_url)
        except Exception as e:
            return None

    class Meta:
        model = VoiceRecording
        fields = "__all__"


class VoiceRecordingSerializer(ModelSerializer):

    class Meta:
        model = VoiceRecording
        fields = "__all__"

