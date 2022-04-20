from django.db import models
from authentication.models import User

# Create your models here.

class Follow(models.Model):
      following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_follows")
      follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_is_followed")
      follow_time = models.DateTimeField(auto_now=True)

      def __unicode__(self):
          return str(self.follow_time)
      
      def __str__(self):
          return str(self.following) + ' --> ' + str(self.follower)