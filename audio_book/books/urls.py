from django.urls import path

from .views import (
    LevelListView,
    LevelDetailView,
    BookDetailView,
    ChapterDetailView,
    last_version_view
)

app_name = 'books'

urlpatterns = [
    path('levels/', LevelListView.as_view(), name='level_list'),
    path('levels/<int:id>/', LevelDetailView.as_view(), name='level_detail'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('chapters/<int:id>/', ChapterDetailView.as_view(), name='chapter_detail'),
    path('versions/last/', last_version_view, name='last_version'),
]
