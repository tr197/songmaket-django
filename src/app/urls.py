from django.contrib import admin
from django.urls import path, include
from app.swagger import swagger_urls


urlpatterns = [
    *swagger_urls,
    path("admin/", admin.site.urls),
    path("auth/", include("authen.urls")),
]
