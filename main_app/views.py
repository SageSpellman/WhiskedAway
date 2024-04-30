from django.shortcuts import render, redirect, requests
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe 

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

class RecipeListView(ListView):

    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'ingredients', 'instructions']

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'ingredients', 'instructions']

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = '/recipes/'
