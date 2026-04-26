from django.db import models
from django.utils import timezone

# POST MODEL
class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title