# In recipes/management/commands/import_recipes.py

from django.core.management.base import BaseCommand
from recipes.models import Recipe, Category
import os
import csv # Make sure csv is imported if it's not already

class Command(BaseCommand):
    help = 'Imports recipes and categories from a CSV file.'

    def handle(self, *args, **options):
        # We have commented these lines out to prevent errors on the first run.
        # self.stdout.write("Deleting old recipe data...")
        # Recipe.objects.all().delete()
        # Category.objects.all().delete()

        csv_file_path = 'index.csv'
        self.stdout.write(f"Starting import from {csv_file_path}...")

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category_name = row['category']
                category_image_name = f"{category_name}.png" 

                if not os.path.exists(os.path.join('media', 'category_cards', category_image_name)):
                     category_image_name = f"{category_name}.jpg"

                category, created = Category.objects.get_or_create(
                    name=category_name,
                    defaults={'image': f'category_cards/{category_image_name}'}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created category: {category_name}'))

                Recipe.objects.create(
                    name=row['recipe_name'],
                    category=category,
                    image=f"images/{row['image_file_1']}"
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported all recipes!'))