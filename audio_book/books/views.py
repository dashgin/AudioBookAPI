from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Level, Book
from .serializers import LevelListSerializer, LevelDetailSerializer, BookDetailSerializer


class LevelListView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelListSerializer


class LevelDetailView(RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelDetailSerializer
    lookup_field = 'id'


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = 'id'
