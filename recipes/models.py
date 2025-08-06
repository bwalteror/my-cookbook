from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # We'll store the path to the category card image
    image = models.ImageField(upload_to='category_cards/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories" # Fixes "Categorys" in admin

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    # A ForeignKey creates a many-to-one link. Many recipes can be in one category.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    # We'll store the path to the main recipe image
    image = models.ImageField(upload_to='images/')
    # --- ADD THESE TWO NEW FIELDS ---
    is_favorite = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    # --------------------------------


    def __str__(self):
        return self.name