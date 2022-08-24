from django.db import models

# Create your models here.

class Cryptocoin(models.Model):
    name        = models.CharField(max_length = 50)
    value       = models.FloatField()
    date_time   = models.DateField()

    def __str__(self):
        return self.date_time+' '+self.name
    