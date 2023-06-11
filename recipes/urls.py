from django.urls import path
from . import views
urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('search/', views.SearchRecipeView, name='search-recipe'),
    path('add_favorite/<int:recipe_id>/', views.AddFavoriteView, name='recipes-add-favorite'),
    path('remove_favorite/<int:recipe_id>/', views.RemoveFavoriteView, name='recipes-remove-favorite'),
    path('favorites/',views.FavoritesView, name='recipes-favorites-views'),
]