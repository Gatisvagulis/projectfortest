from django.db import models
import uuid

class Programminglanguages(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
