from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogList(APIView):

    def get(self, request: Request, format=None) -> Response:

        Dogs = Dog.objects.all()
        serialiser = DogSerializer(Dogs, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def put(self, request: Request, format=None) -> Response:

        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
