from django.shortcuts import render
from rest_framework.views import APIView # с помощью него будем расширять наше приложение
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed # исключение, если пользователь не тот

class RegisterView(APIView):
    def post(self, request):
         serializer = UserSerializer(data=request.data) # данне по реквест запросу
         serializer.is_valid(raise_exception=True) # проверка данных на валидность
         serializer.save()
         return Response(serializer.data)

class LoginView(APIView): # класс входа в систему
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None: # если пользователь не тот
            raise AuthenticationFailed('Пользователь не найден')

        if not user.check_password(password): # если пароль не тот
            raise AuthenticationFailed('неверный пароль')

        return Response(user)