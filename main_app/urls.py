from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/add/<int:recipe_id>/', views.add_favorite, name='add_favorite'),
    path('favorites/remove/<int:favorite_id>/', views.remove_favorite, name='remove_favorite'),
    path('favorites/edit/<int:favorite_id>/', views.edit_favorite, name='edit_favorite'),
]