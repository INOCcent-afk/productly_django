from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path("api/v1.0/products/", views.products),
]
