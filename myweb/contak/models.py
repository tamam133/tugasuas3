from django.db import models

class contak(models.Model):
    platfom = models.CharField(max_length=50)
    pesan = models.CharField(max_length=50)
