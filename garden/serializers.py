from rest_framework import serializers
from .models import Garden, GardenPlant, Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            'id',
            'name',
            'inches_between_plants',
            'inches_between_rows',
            'depth_inches',
            'days_to_germinate',
            'days_to_harvest',
            'notes'
        )

class GardenPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = GardenPlant
        plant = PlantSerializer(many=False)
        fields = (
            'garden',
            'plant',
            'number_planted',
            'date_planted'
        )

class GardenSerializer(serializers.ModelSerializer):
    plants = serializers.SerializerMethodField()

    class Meta:
        model = Garden
        fields = (
            'id',
            'name',
            'square_feet',
            'plants'
        )

    def get_plants(self, obj):
        garden_plants = obj.plants.all()
        serializer = GardenPlantSerializer(garden_plants, many=True, read_only=True)

        return serializer.data
