# from django.shortcuts import render
# from .models import Movie

# def base(request):
#     return render(request,'base.html')

# def movie_list(request):
#     qs=Movie.objects.all()
#     return render(request,'movie_list.html',{'qs':qs})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from django.contrib import messages

def base(request):
    return render(request, 'base.html')

def movie_list(request):
    qs = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'qs': qs})

def movie_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')
        personal_notes = request.POST.get('personal_notes')
        watched = request.POST.get('watched') == 'on'
        poster = request.FILES.get('poster')

        Movie.objects.create(
            title=title,
            director=director,
            genre=genre,
            release_year=release_year,
            rating=rating,
            personal_notes=personal_notes,
            watched=watched,
            poster=poster
        )
        messages.add_message(request,messages.SUCCESS,'Movie added successfully')
        return redirect('movie_list')  # Redirect to the movie list page after adding
    return render(request, 'movies/movie_add.html')

def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    if request.method == 'POST':
        movie.title = request.POST.get('title', movie.title)
        movie.director = request.POST.get('director', movie.director)
        movie.genre = request.POST.get('genre', movie.genre)
        movie.release_year = request.POST.get('release_year', movie.release_year)
        movie.rating = request.POST.get('rating', movie.rating)
        movie.personal_notes = request.POST.get('personal_notes', movie.personal_notes)
        movie.watched = request.POST.get('watched', movie.watched) == 'on'
        if 'poster' in request.FILES:
            movie.poster = request.FILES['poster']
        movie.save()
        messages.add_message(request,messages.SUCCESS,'Movie updated successfully')
        return redirect('movie_list')
    
    return render(request, 'movies/movie_edit.html', {'movie': movie})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        messages.add_message(request,messages.SUCCESS,'Movie deleted successfully')
        return redirect('movie_list')  # Redirect to the movie list page after deleting
    return render(request, 'movies/movie_delete.html', {'movie': movie})
