from django.urls import path
from . import views

urlpatterns = [
    path("", views.NoteApiView.as_view()),
    path("<int:pk>/", views.NoteDeatilApiView.as_view()),
]