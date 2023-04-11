from django.shortcuts import render
from rest_framework.views import APIView # с помощью него будем расширять наше приложение
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed # исключение, если пользователь не тот
import jwt, datetime

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

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=300),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
            }

        return response