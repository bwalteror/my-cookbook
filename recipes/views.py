from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe
from django.db.models import F # <-- ADD THIS IMPORT

def category_list(request):
    categories = Category.objects.all().order_by('name')
    # Path to the recipe box image
    recipe_box_image = 'src/media/master_image/RECIPE BOX.jpg'
    context = {
        'categories': categories,
        'recipe_box_image': recipe_box_image,
    }
    return render(request, 'recipes/category_list.html', context)
    
def recipe_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    # Get all recipes for this category, ordered by name
    recipes = category.recipes.all().order_by('name')
    context = {
        'category': category,
        'recipes': recipes,
    }
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Atomically increment the view_count by 1
    Recipe.objects.filter(pk=pk).update(view_count=F('view_count') + 1)
    
    # We need to refresh the object from the DB to get the updated count
    recipe.refresh_from_db()
    
    context = {
        'recipe': recipe,w
    }
    breakpoint()    
    return render(request, 'recipes/recipe_detail.html', context)

# Add this new function to the end of recipes/views.py

def search_results(request):
    # Get the search query from the URL's 'q' parameter
    query = request.GET.get('q')
    
    if query:
        # Filter recipes where the name contains the query (case-insensitive)
        recipes = Recipe.objects.filter(name__icontains=query)
    else:
        # If no query, return no recipes
        recipes = Recipe.objects.none()
        
    context = {
        'recipes': recipes,
        'query': query,
    }
    return render(request, 'recipes/search_results.html', context)
    # Add this new function to the end of recipes/views.py

def about_page(request):
    return render(request, 'recipes/about.html')
    
    # Add this to the end of recipes/views.py
def favorites_list(request):
    # Get all recipes that are marked as a favorite
    favorite_recipes = Recipe.objects.filter(is_favorite=True).order_by('name')
    context = {
        'recipes': favorite_recipes
    }
    return render(request, 'recipes/favorites_list.html', context)
    