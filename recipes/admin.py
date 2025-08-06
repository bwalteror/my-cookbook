# In recipes/admin.py

from django.contrib import admin
from .models import Category, Recipe

# Customize how the Recipe model is displayed in the admin
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_favorite', 'view_count')
    list_filter = ('category', 'is_favorite')
    search_fields = ('name',)
    # This makes the 'is_favorite' checkbox clickable directly in the list!
    list_editable = ('is_favorite',)
    # This prevents accidental editing of the view count
    readonly_fields = ('view_count',)

# A simple registration for the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)