from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]