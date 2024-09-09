from django.db import models
from django.contrib.auth.models import User

class SignalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event} for {self.user.username} at {self.timestamp}"