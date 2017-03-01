from django.db import models
import uuid
from mptt.models import MPTTModel, TreeForeignKey


class Channel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    channel = models.ForeignKey(Channel, related_name="categories")
    parent = TreeForeignKey("self", related_name="children", blank=True,
                            null=True, db_index=True)

    class MPTTMeta:
        db_table = "categories"
        order_insertion_by = ['name']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
