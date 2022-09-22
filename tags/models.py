from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.

class LikedItem(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    # ContentType for identifying the kind of object the user likes.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Object ID for referencing that particular object
    object_id = models.PositiveIntegerField()
    # Content Object for reading the particular object.
    content_object = GenericForeignKey()

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()