from django.urls import path

from .views import (
    LevelListView,
    LevelDetailView,
    BookDetailView
)

app_name = 'books'

urlpatterns = [
    path('levels/', LevelListView.as_view(), name='level_list'),
    path('levels/<int:id>/', LevelDetailView.as_view(), name='level_detail'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
]
