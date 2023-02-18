from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=80, blank=False, default="")
    description = models.CharField(max_length=500, blank=False, default="")
    release_date = models.DateField()
