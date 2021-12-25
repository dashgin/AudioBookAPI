from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Level, Book, Chapter
from .serializers import (
    LevelListSerializer,
    LevelDetailSerializer,
    BookDetailSerializer,
    ChapterDetailSerializer,
)


class LevelListView(ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelListSerializer


class LevelDetailView(RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelDetailSerializer
    lookup_field = "id"


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = "id"


class ChapterDetailView(RetrieveAPIView):
    """
    return a chapter from given id
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterDetailSerializer
    lookup_field = "id"