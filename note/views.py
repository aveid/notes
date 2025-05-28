from rest_framework import generics, status
from django.db.models import Q
from .permissions import AuthorOrReadOnly
from .serializers import NoteSerializer
from note.models import Note



class NoteApiView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer



    def get_queryset(self):
        queryset = Note.objects.filter(
            Q(is_private=False) |
        Q(is_private=True, user=self.request.user))
        return queryset


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDeatilApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AuthorOrReadOnly, ]
