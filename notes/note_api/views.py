from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import NoteModel
from .serializers import NoteSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
# class NoteList(generics.ListAPIView):
#     serializer_class = NoteSerializer
#     queryset = NoteModel.objects.all()

# class NoteCreate(generics.CreateAPIView):
    
#     serializer_class = NoteSerializer
#     queryset = NoteModel.objects.all()
#     permission_classes = [IsAuthenticated]

    

        

# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = NoteSerializer
#     queryset = NoteModel.objects.all()
#     permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer