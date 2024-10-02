from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serialisers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class= NoteSerializer
    permission_classes = [IsAuthenticated]

    # this will get the notes related to the user
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    # this function will take the input from the json frontend and pass it to the serializer to check if it is valid and then save it to the db
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else: 
            print(serializer.errors)
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
