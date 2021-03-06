from django.db import models


class Level(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.number)


class Book(models.Model):
    title = models.CharField(max_length=100)
    level = models.ForeignKey(Level, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    book = models.ForeignKey(Book, related_name="chapters", on_delete=models.CASCADE)
    audio = models.FileField(upload_to="audio/")
    subtitle = models.FileField(upload_to="subtitle/")

    def __str__(self):
        return self.title


class Version(models.Model):
    version = models.CharField(max_length=10)
    release_date = models.DateField()
    change_log = models.TextField()

    def __str__(self):
        return self.version
