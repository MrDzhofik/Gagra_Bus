from django.db import models

# Create your models here.
class Town(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=5)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Stop(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Route_Stop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    ordinal_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.route} - {self.stop}"
    
class Schedule(models.Model):
    route_stop = models.ForeignKey(Route_Stop, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"{self.route_stop} - {self.time}"
