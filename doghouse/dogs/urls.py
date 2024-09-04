from django.urls import path

from .views import DogList, DogDetail

urlpatterns = [
    path("dogs/", DogList.as_view()),
    path("dogs/<int:pk>", DogDetail.as_view()),
]
