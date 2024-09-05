from django.urls import path, include

# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import DogList, DogDetail, BreedList

router = DefaultRouter()
router.register("breeds", BreedList, "breeds")

urlpatterns = [
    path("dogs/", DogList.as_view()),
    path("dogs/<int:pk>", DogDetail.as_view()),
    path("", include(router.urls)),
]
