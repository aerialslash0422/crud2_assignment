from django.urls import path
from .views import *

urlpatterns = [
    path('/movie', MovieView.as_view()), # ow
    path('/actor',ActorView.as_view()),       
]
