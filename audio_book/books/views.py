from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Level, Book, Chapter, Version
from .serializers import (
    LevelListSerializer,
    LevelDetailSerializer,
    BookDetailSerializer,
    ChapterDetailSerializer,
    VersionSerializer,
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


class LastVersionApiView(APIView):
    """
    return a current version of the app
    """

    serializer_class = VersionSerializer

    def get(self, request):
        version = Version.objects.last()
        serializer = self.serializer_class(version)
        return Response(serializer.data, status=status.HTTP_200_OK)

last_version_view = LastVersionApiView.as_view()