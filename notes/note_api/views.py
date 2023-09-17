from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from .models import NoteModel
from .serializers import NoteSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class NoteList(generics.ListAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

class NoteCreate(generics.CreateAPIView):
    # user = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    # )
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()
    permission_classes = [IsAuthenticated]

    

        

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]