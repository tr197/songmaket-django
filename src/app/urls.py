from django.contrib import admin
from django.urls import path, include
from app.swagger import swagger_urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    *swagger_urls,
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path("admin/", admin.site.urls),
    path("auth/", include("authen.urls")),
]
