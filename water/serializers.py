
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password= serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


    def validate(self, attrs):
        email=attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'(Email is already in use)'})
        return super().validate(attrs)

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)