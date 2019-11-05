from .models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user = User.objects.create(
            creating_profile_for=validated_data['creating_profile_for'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            contactNo=validated_data['contactNo'],
            email=validated_data['email'],
            password=validated_data['password'],
            confirm=validated_data['confirm']
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ('token', 'creating_profile_for', 'first_name', 'middle_name', 'last_name', 'gender', 'contactNo', 'email', 'password', 'confirm')