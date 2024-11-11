from django.urls import path

from . import views

urlpatterns = [
    path("img/<str:file_name>", views.image, name="img"),
    path("", views.ResponseSettingsUpdateView.as_view(), name="index"),
]
