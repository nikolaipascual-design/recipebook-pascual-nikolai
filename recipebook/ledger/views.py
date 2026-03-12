from django.shortcuts import render
from .models import Ingredient, Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view')

def recipes(request):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2cup"
                    },
                    {
                        "name": "water",
                        "quanity": "1 cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "/recipe/2"
            }
        ]
    }
    return render(request, "ledger/recipes/list.html", ctx)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'

    def get_queryset(self):
        return Ingredient.objects.filter(recipe__recipe__name = "Recipe 1")
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/list.html'

class LoginView(LoginView):
    template_name = 'ledger/recipe/login.html'