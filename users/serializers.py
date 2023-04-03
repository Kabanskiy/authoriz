from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'username', 'email', 'password'] # здесь будем создавать поля для нового пользователя
        extra_kwargs = {"password":{"write_only":True}}

        def create(self, validated_data): # функция для хеширования пароля
            password = validated_data.pop("password", None)
            instance = self.Meta.model(**validated_data)
            if password is not None: # если пароль не равен нулю, то мы будем его хешировать, т.е. ставить пароль для пароля
                instance.set_password(password)
            instance.save()
            return instance
