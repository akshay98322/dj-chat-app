from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    content  = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
