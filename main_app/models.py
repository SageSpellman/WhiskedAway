from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    difficulty = models.TextField()
    portion = models.TextField()
    time = models.TextField()
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('add_recipes')