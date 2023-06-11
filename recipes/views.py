
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


def home(request):
    recipes = models.Recipe.objects.all()
    context ={
        'recipes':recipes
    }
    return render(request, "recipes/home.html", context)

def SearchRecipeView(request):
    query = request.GET.get('q')
    recipes = models.Recipe.objects.filter(title__icontains=query)
    return render(request, 'recipes/search_recipe.html', {'recipes': recipes, 'query': query})

class RecipeListView(ListView):
    model = models.Recipe
    template_name = "recipes/home.html"
    context_object_name = 'recipes'
class RecipeDetailView(DetailView):
    model = models.Recipe

class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = models.Recipe
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title','description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author




