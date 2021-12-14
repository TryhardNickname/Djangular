from django.db import models

# Create your models here.
class Tutorial(models.Model):
    string = models.CharField(max_length=200,blank=False, default='')