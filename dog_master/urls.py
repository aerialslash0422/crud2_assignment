from django.urls import path
from .views import *

urlpatterns = [
    path('/owners', OwnerView.as_view()), # ow
    path('/ownerswithdog',OwnerWithDogView.as_view()),
    path('/dogs', DogView.as_view()),
        
]
