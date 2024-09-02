from django.db import models

class Movie(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    personal_notes = models.TextField(blank=True)
    watched = models.BooleanField(default=False)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)  # New field added

    def __str__(self):
        return self.title
