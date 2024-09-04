from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedList(APIView):

    def get(self, request: Request, format=None) -> Response:

        breeds = Breed.objects.all()
        serialiser = BreedSerializer(breeds, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def put(self, request: Request, format=None) -> Response:

        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
