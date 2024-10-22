from django.db import models
from django.contrib.auth.models import User
from teams.models import ProjectTeam

# Create your models here.
class Project(models.Model):
    """
    A model for a project.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
