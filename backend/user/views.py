from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserCreateSerializer, UserSerializer

class HealthCheck(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"status": "ok"})
    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        
        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)
        
        return Response(user.data, status=status.HTTP_201_CREATED)
    
class RetriveUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        user = UserSerializer(user)
        
        return Response(user.data, status=status.HTTP_200_OK)