from django.db import models

# Create your models here.
class folder_readed(models.Model):
    date = models.DateTimeField(auto_now=True)
    folder = models.CharField(max_length=1000)