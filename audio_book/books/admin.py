from django.contrib import admin

from .models import Level, Book, Chapter, Version


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('number',)


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'level',)
    list_filter = ('title',)
    inlines = [ChapterInline]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'release_date', 'change_log',)
    list_filter = ('version',)