from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid
import shortuuid


class Channel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = shortuuid.encode(self.id)
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(MPTTModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    channel = models.ForeignKey(Channel, related_name="categories")
    parent = TreeForeignKey("self", related_name="children", blank=True,
                            null=True, db_index=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = shortuuid.encode(self.id)
        super(Category, self).save(*args, **kwargs)

    class MPTTMeta:
        db_table = "categories"
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
