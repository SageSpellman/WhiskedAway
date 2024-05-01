from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('favorites/', views.FavoriteList.as_view(), name='favorites_index'),
    path('favorites/<int:pk>/', views.FavoriteDetail.as_view(), name='favorites_detail'),
    path('favorites/add/<int:recipe_id>/', views.add_favorite, name='add_favorite'),
]