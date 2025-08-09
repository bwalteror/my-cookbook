# cookbook/urls.py

from django.contrib import admin
from django.urls import path, include

# These two imports are essential for serving files in production
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]

# This line is the fix. It adds a URL pattern for your media files.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)