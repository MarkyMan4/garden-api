from django.db import models

class Garden(models.Model):
    name = models.CharField(null=False, max_length=500)
    square_feet = models.DecimalField(null=False, max_digits=12, decimal_places=2)

# information about plants
class Plant(models.Model):
    name = models.CharField(null=False, max_length=200)
    inches_between_plants = models.IntegerField(null=False)
    inches_between_rows = models.IntegerField(null=False)
    depth_inches = models.DecimalField(null=False, max_digits=3, decimal_places=2)
    days_to_germinate = models.IntegerField(null=False)
    days_to_harvest = models.IntegerField(null=False)
    notes = models.CharField(null=True, max_length=1000)

# plants that have been put into a garden
class GardenPlant(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    number_planted = models.IntegerField(null=False)
    date_planted = models.DateField(null=False)
