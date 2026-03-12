from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.name)])


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete = models.CASCADE,
        related_name = 'ingredients'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        related_name = 'recipe'
    )

class Profile(models.Model):
    user = models.OneToOneField(get_user_model, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)