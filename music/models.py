from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=25)
    text = models.TextField()
    user = models.ForeignKey(User)
    description = models.TextField(max_length=40)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

class Single(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=25)
    link = models.FileField()

    def __str__(self):
        return self.title

class Album(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=25)
    timing = models.TextField(max_length=8)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.title

class Actual(models.Model):
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True)
    audio = models.FileField(blank=True)
    video = models.URLField(blank=True)

class ActualAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = Actual.objects.all().count()
    if count == 0:
      return True

    return False