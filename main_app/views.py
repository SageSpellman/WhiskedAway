from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Recipe, Favorite
import requests, os

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def recipes(request): 
    url = "https://the-vegan-recipes-db.p.rapidapi.com/"

    headers = {
	"X-RapidAPI-Key": os.getenv('API_KEY'),
	"X-RapidAPI-Host": "the-vegan-recipes-db.p.rapidapi.com"
}
    response = requests.get(url, headers=headers)
    response = response.json()
    return render(request, 'recipes/index.html', {'recipes':response})

def recipes_detail(request, recipe_id):
    url = f"https://the-vegan-recipes-db.p.rapidapi.com/{recipe_id}"

    headers = {
	"X-RapidAPI-Key": os.getenv('API_KEY'),
	"X-RapidAPI-Host": "the-vegan-recipes-db.p.rapidapi.com"
}
    response = requests.get(url, headers=headers)
    response = response.json()
    return render(request, 'recipes/detail.html', {'recipe':response})

@login_required
def add_favorite(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    Favorite.objects.create(user=request.user, recipe=recipe)
    return redirect('favorites')

@login_required
def remove_favorite(request, favorite_id):
    favorite = Favorite.objects.get(pk=favorite_id)
    favorite.delete()
    return redirect('favorites')

@login_required
def edit_favorite(request, favorite_id):
    favorite = Favorite.objects.get(pk=favorite_id)
    return redirect('favorites')

@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})