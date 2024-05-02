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
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.recipe_name} by {self.user.username}"
    
    def get_absolute_url(self):
        return reverse('review_list')