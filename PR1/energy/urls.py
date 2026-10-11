from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("objects/", include("objects.urls")),
    path("meters/", include("meters.urls")),
    path("readings/", include("readings.urls")),
]

handler404 = "homepage.views.page_not_found"
