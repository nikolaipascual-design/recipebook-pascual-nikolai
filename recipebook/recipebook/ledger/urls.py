from django.urls import path

from .views import index
from .views import recipes

urlpatterns = [
    path('', index, name='index'),
    path('recipes', recipes, name='recipes')
]

app_name = "ledger"