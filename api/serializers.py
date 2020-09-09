from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            user_mobile_no = validated_data['user_mobile_no'],
            password = make_password(validated_data['password']),
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            # is_staff = validated_data['is_staff'],
            # is_active = validated_data['is_active'],
            user_address = validated_data['user_address']
        )
        user.save()
        return user
    def update(self, instance,validated_data):
        user = User.objects.get(pk=instance.id)
        user.password = make_password(validated_data['password'])
        user.username = validated_data['username']
        user.email = validated_data['email']
        user.user_address = validated_data['user_address']
        user.user_mobile_no = validated_data['user_mobile_no']
        # user.is_active = validated_data['is_active']
        # user.is_staff = validated_data['is_staff']
        # user.is_superuser = validated_data['is_superuser']
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name','is_staff','is_active','is_superuser','user_address','user_mobile_no']
        read_only_fields = ('is_active', 'is_staff', 'is_superuser')
        write_only_fields = ('password')
        