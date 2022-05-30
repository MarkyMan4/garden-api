from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from garden.serializers import GardenPlantSerializer, GardenSerializer, PlantSerializer
from garden.models import Garden, GardenPlant, Plant

class PlantViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Plant.objects.all()

    # GET /api/plants
    def list(self, request):
        plants = self.get_queryset()
        serializer = PlantSerializer(plants, many=True)

        return Response(serializer.data)

    # GET /api/plants/<id>
    def retrieve(self, request, pk):
        plant_queryset = self.get_queryset().filter(id=pk)
        plant = get_object_or_404(plant_queryset)
        serializer = PlantSerializer(plant, many=False)

        return Response(serializer.data)

class GardenViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Garden.objects.all()

    # POST /api/garden
    def create(self, request):
        data = request.data
        serializer = GardenSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # GET /api/garden
    def list(self, request):
        gardens = self.get_queryset()
        serializer = GardenSerializer(gardens, many=True)

        return Response(serializer.data)

    # GET /api/garden/<id>
    def retrieve(self, request, pk):
        garden_queryset = self.get_queryset().filter(id=pk)
        garden = get_object_or_404(garden_queryset)
        serializer = GardenSerializer(garden, many=False)

        return Response(serializer.data)

class GardenPlantViewSet(viewsets.ViewSet):
    # POST /api/gardenplant
    def create(self, request):
        data = request.data
        serializer = GardenPlantSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

