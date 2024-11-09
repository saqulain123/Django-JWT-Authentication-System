from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import UserData
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Fetch all users from the UserData model
        users = UserData.objects.all()
        # Serialize the data to send in the response
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
