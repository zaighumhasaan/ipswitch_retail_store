
"""
URL configuration for ipswich_retail project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "healthy", "service": "ipswich-retail"})


urlpatterns = [
    path("health/", health_check, name="health"),
    path("admin/", admin.site.urls),
    path("", include("store.urls")),
]

# ✅ Always serve media files (even when DEBUG = False)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
