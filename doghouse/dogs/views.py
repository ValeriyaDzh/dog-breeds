from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogList(APIView):

    def get(self, request: Request, format=None) -> Response:
        dogs = Dog.objects.all()
        serialiser = DogSerializer(dogs, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None) -> Response:
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):

    def _get_dog(self, pk: int) -> Dog:
        try:
            return Dog.objects.get(pk=pk)

        except Dog.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int, format=None) -> Response:
        dog = self._get_dog(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None) -> Response:
        dog = self._get_dog(pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None) -> Response:
        dog = self._get_dog(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(ViewSet):

    def list(self, request: Request, format=None) -> Response:
        breeds = Breed.objects.all()
        serialiser = BreedSerializer(breeds, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def create(self, request: Request, format=None) -> Response:
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(ViewSet):

    def _get_breed(self, pk: int) -> Breed:
        try:
            return Breed.objects.get(pk=pk)

        except Breed.DoesNotExist:
            raise Http404

    def retrieve(self, request: Request, pk: int) -> Response:
        breeds = self._get_breed(pk)
        serializer = BreedSerializer(breeds)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request: Request, pk: int) -> Response:
        breed = self._get_breed(pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int) -> Response:
        Breed = self._get_breed(pk)
        Breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
