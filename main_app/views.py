from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
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

def add_favorite(request, recipe_id):
    favorite = Favorite( recipe=recipe_id)
    favorite.save()
    return redirect('favorites')

class FavoriteList(ListView):
    model = Favorite

class FavoriteDetail(DetailView):
    model = Favorite