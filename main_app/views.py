from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, Review
import requests, os

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            recipe = Recipe(
                user=request.user,
                title=title,
                difficulty=request.POST.get('difficulty'),
                portion=request.POST.get('portion'),
                time=request.POST.get('time'),
                description=request.POST.get('description'),
                ingredients=request.POST.get('ingredients'),
                instructions=request.POST.get('instructions'),
            )
            recipe.save()
    recipes = request.user.recipe_set.all()
    return render(request, 'main_app/add_recipes.html', {'recipes':recipes})

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['ingredients', 'difficulty']
  url = '/add_recipes/'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes'

class ReviewList(ListView):
    model = Review
    template_name = 'main_app/review_list.html'  

class ReviewDetail(DetailView):
    model = Review
    template_name = 'main_app/review_detail.html' 

class ReviewCreate(CreateView):
    model = Review
    fields = ['recipe_name', 'rating', 'review']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['rating', 'review']
    template_name = 'main_app/review_form.html' 

class ReviewDelete(DeleteView):
    model = Review
    success_url = '/reviews'