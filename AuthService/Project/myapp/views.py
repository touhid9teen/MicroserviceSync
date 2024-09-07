from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, CustomUserRegistationSerializer
from .authenticate import CustomAuthentication
from . models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta, datetime, timezone
import jwt



class RegisterView(APIView):
    authentication_classes = []

    def post(self, request):
        MySerializer = CustomUserRegistationSerializer(data=request.data)
        if MySerializer.is_valid():
            MySerializer.save()
            return Response(MySerializer.data, status=status.HTTP_201_CREATED)
        return Response(MySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(email=email)

            if not user:
                return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Generate a token using the RSA private key
            token = self.generate_token(user)
            return Response({"access_token": token}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def generate_token(self, user):
        # Load the RSA private key from the file
        with open("keys/private_key.pem", "r") as priv_key_file:
            private_key = priv_key_file.read()

        # Create JWT payload
        payload = {
            "user_id": user.id,
            "name": user.name,
            "exp":  datetime.now(timezone.utc)+ timedelta(hours=1)  # Token expiration time
        }

        # Encode the JWT token using the RSA private key
        token = jwt.encode(payload, private_key, algorithm='RS256')
        return token

class UserInfoView(APIView):
    authentication_classes = [CustomAuthentication]

    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PublicKeyView(APIView):
    def get(self, request):
        public_key_path = "./keys/public_key.pem"
        try:
            with open(public_key_path, "r") as f:
                public_key = f.read()
            return Response({"public_key": public_key}, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({"error": "Public key not found"}, status=status.HTTP_404_NOT_FOUND)