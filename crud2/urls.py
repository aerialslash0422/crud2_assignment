from django.urls import include, path

urlpatterns = [
    path('dog_master', include('dog_master.urls'))
]
