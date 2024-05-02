from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('recipes/add/', views.add_recipes, name='add_recipes'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='reviews_detail'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='reviews_create'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete'),
]