from django.db import models

class weather(models.Model):
    weather = models.CharField(max_length=10)
    def __str__(self):
        return self.weather
