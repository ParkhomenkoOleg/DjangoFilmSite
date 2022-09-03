from django.db import models
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    ratings = models.CharField(max_length=255)
    release = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    age_for_watching = models.CharField(max_length=3)
    country = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    trailer = models.URLField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('film', kwargs={'film_name': self.title})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_name': self.name})
