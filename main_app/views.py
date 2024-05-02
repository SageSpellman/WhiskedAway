from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Recipe
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

def add_recipes(request):
    title = request.POST.get('title')
    if title:
        recipe = Recipe(
            title=title,
            difficulty=request.POST.get('difficulty'),
            portion=request.POST.get('portion'),
            time=request.POST.get('time'),
            description=request.POST.get('description'),
            ingredients=request.POST.get('ingredients'),
            instructions=request.POST.get('instructions'),
        )
        recipe.save()
    return render(request, 'main_app/add_recipes.html')