# recipes/urls.py

from django.urls import path
from . import views
# recipes/urls.py
# ... (imports) ...

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('search/', views.search_results, name='search_results'),
    path('about/', views.about_page, name='about_page'), # ADD THIS LINE
    path('favorites/', views.favorites_list, name='favorites_list'), # ADD THIS
    path('category/<int:pk>/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]