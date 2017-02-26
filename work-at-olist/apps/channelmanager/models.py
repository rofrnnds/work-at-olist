from django.db import models


class Channel(models.Model):

    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=120)
    channel = models.ForeignKey(Channel, related_name="categories")
    parent = models.ForeignKey(
        "self", related_name="children", blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
