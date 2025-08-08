"""
URL configuration for cookbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# FILE: cookbook/urls.py

from django.contrib import admin
from django.urls import path, include

# These two imports are required for this to work!
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]

# This line tells Django how to serve media files in production.
# It MUST be present and NOT wrapped in an 'if' statement.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
