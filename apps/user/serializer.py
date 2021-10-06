from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from common.enum import Types
from .models import User

type_obj = Types()


class UserSerializer(ModelSerializer):
    username = CharField(max_length=120, required=True, allow_null=False)
    first_name = CharField(max_length=100, required=True, allow_null=False)
    last_name = CharField(max_length=50, required=True, allow_null=False)
    email = EmailField(required=True, allow_null=False)
    date_of_birth = DateField(required=False, allow_null=True)
    user_image = ImageField(required=False, allow_null=True)
    created_by_id = IntegerField(required=False, allow_null=True)
    status = CharField(required=False, default=1)
    type = CharField(required=False, allow_null=True)

    def validate_type(self, value):
        type_value = type_obj.get_user_type(value)
        if type_value == 0:
            raise ValidationError("Invalid Type.")
        return type_value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'unique_code', 'username', 'date_of_birth',
                  'user_image', 'password', 'created_by_id', 'type',
                  'status']


class GetUserSerializer(ModelSerializer):
    user_image = SerializerMethodField('get_user_image', required=False)
    type = SerializerMethodField('get_type', required=False)
    status = SerializerMethodField('get_status', required=False)

    def get_user_image(self, obj):
        try:
            photo_url = obj.user_image.url
            # print("PHOTO URL: ", photo_url)
            return self.context['request'].build_absolute_uri(photo_url)
        except Exception as e:
            # print(e)
            return None

    def get_type(self, obj):
        return type_obj.get_user_type(obj.type)

    def get_status(self, obj):
        return type_obj.get_status(status=obj.status)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'date_of_birth', 'user_image', 'type',
                  'created_by_id',
                  'status', 'date_joined']


class UpdateUserSerializer(ModelSerializer):
    os = CharField(max_length=10, required=True, allow_null=False)
    type = CharField(required=False, allow_null=False)
    status = CharField(required=False, allow_null=False)
    modified_by_id = IntegerField(required=True, allow_null=False)

    def validate_type(self, value):
        type_value = type_obj.get_user_type(user_type=value)
        if type_value == 0:
            raise ValidationError("Invalid Type.")
        return type_value

    def validate_status(self, value):
        status_value = type_obj.get_status(status=value)
        if status_value == 0:
            raise ValidationError("Invalid Status.")
        return status_value

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'date_of_birth',
                  'user_image', 'type', 'modified_by_id',
                  'modified_datetime', 'status', 'date_joined']


class FilterUserSerializer(ModelSerializer):
    type = CharField(required=False, allow_null=False)
    status = CharField(required=False, allow_null=False)

    def validate_type(self, value):
        type_value = type_obj.get_user_type(user_type=value)
        if type_value == 0:
            raise ValidationError("Invalid Type.")
        return type_value

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'date_of_birth', 'user_image', 'type',
                  'modified_by_id',
                  'modified_datetime', 'status', 'date_joined']


class LoginSerializer(ModelSerializer):
    username = CharField(max_length=50, required=True, allow_null=False)
    password = CharField(max_length=50, required=True, allow_null=False)
    type = CharField(max_length=35, required=False, allow_null=False)

    def validate_type(self, value):
        type_value = type_obj.get_user_type(value)
        if type_value == 0:
            raise ValidationError("Invalid Type.")
        return type_value

    class Meta:
        model = User
        fields = ['username', 'password', 'type']


