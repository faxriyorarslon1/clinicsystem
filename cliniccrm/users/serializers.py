from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User



class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'last_name','password',
                  'middlename', 'phone', 'gender')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def to_representation(self, ins):
        return {
            "id": ins.id,
            "email": ins.email,
            "username": ins.username,
            "last_name": ins.last_name,
            "middlename": ins.middlename,
            "phone": ins.phone,
            "gender": ins.gender,
        }