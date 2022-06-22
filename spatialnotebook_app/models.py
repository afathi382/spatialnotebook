from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.PointField()
    
    
    def __str__(self):
        return self.title