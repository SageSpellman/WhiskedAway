from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail')
]