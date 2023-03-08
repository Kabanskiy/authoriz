from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'username', 'email', 'password'] # здесь будем создавать поля для нового пользователя
        extra_kwargs = {"password":{"write_only":True}}

        def create(self, validated_data):
            password=validated_data.pop("password", None)
            intance = self.Meta.model(**validated_data)
            if password is not None:
                intance.set_password(password)
            intance.save()
            return intance
