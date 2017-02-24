from django.db import models


class Channel(models.Model):

    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        self.name
