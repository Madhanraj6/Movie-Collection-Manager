from django.contrib import admin
from .models import Movie
# Register your models here.
@admin.register(Movie)
class Moviemodeladmin(admin.ModelAdmin):
    list_display=['user','title','director']
