from rest_framework import serializers

from .models import Level, Book, Chapter


class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'audio', 'subtitle')


class BookListSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(source='level.number')

    class Meta:
        model = Book
        fields = ('id', 'title', 'level',)
        read_only_fields = [f for f in fields]


class BookDetailSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(source='level.number')
    chapters = ChapterListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'level', 'chapters')
        read_only_fields = [f for f in fields]


class LevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'number',)


class LevelDetailSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = ('id', 'number', 'books',)
