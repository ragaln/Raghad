from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='club_images/')  # Assumes you have set MEDIA_URL and MEDIA_ROOT


    def __str__(self):
        return f"{self.name} ({self.sport.name})"