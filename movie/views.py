import json

from django.views import View
from django.http import JsonResponse

from .models import Actor, Movie, Actor_Movie

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []
        for actor in actors:
            actors_movies = Actor_Movie.objects.filter(actor_id = actor.id)
            movie_list = []
            for actor_movie in actors_movies:
                movie_list.append(
                    {
                        'title' : actor_movie.movie.title
                    }
                )
            # movie_list = [{'title' : actor_movie.movie.title} for actor_movie in actors_movies ]
            result.append(
                    {
                    'Name'        : actor_movie.actor.first_name + actor_movie.actor.last_name,
                    'Birth'       : actor_movie.actor.date_of_birth,
                    'Filmography' : movie_list
                    }    
                )
            
        return JsonResponse({"Actors" : result}, status=200)

        

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []
        for movie in movies:
            actors_movies = Actor_Movie.objects.filter(movie_id = movie.id)
            actor_list = []
            for actor_movie in actors_movies:
                actor_list.append(
                    {
                        'Name': actor_movie.actor.first_name + actor_movie.actor.last_name
                    }
                )
            # actor_list = [{'Name': actor_movie.actor.first_name + actor_movie.actor.last_name} for actor_movie in actors_movies]
            result.append(
                    {
                    'Title'  : actor_movie.movie.title,
                    'Release_Date' : actor_movie.movie.release_date,
                    'Running_Time' : actor_movie.movie.running_time,
                    'Actor' : actor_list
                    }    
                )
            
            
        return JsonResponse({"Movies" : result}, status=200)
    
                