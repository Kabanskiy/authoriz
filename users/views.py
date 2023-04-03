from django.shortcuts import render
from rest_framework.views import APIView # с помощью него будем расширять наше приложение
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed

class RegisterView(APIView):
    def post(self, request):
         serializer = UserSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        pasword = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Пользователь не найден')

        if not user.check_password(password):
            raise AuthenticationFailed('неверный пароль')

        return Response(user)