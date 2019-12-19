from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class AdminTeam(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    socialshare = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Team(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
class Testimonials(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.name



