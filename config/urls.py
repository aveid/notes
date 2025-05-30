from django.contrib import admin
from django.urls import path, include
from .drf_yasg_url import urlpatterns as swagger_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("notes/", include("note.urls")),
    path("comments/", include("comment.urls")),

]
urlpatterns += swagger_url

