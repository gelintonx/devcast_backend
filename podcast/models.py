from django.db import models
from authentication.models import User


class Podcast(models.Model):
    name = models.CharField(max_length=120, blank=True)
    owner = models.ManyToManyField(to=User)
    audio_url = models.URLField()
    description = models.TextField()
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        user = ' & '.join(str(o)for o in self.owner.all())
        return self.name + ' by ' + user
