from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.sport.name})"