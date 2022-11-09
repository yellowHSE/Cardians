from django.db import models

class weather(models.Model):
    weather = models.CharField(max_length=10)
    def __str__(self):
        return self.weather
        
class Sensor(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    watersensor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor'