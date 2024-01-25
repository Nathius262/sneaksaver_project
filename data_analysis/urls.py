from django.urls import path
from .views import search_view

name = "data_analysis"

urlpatterns = [
    path('search/', search_view, name="search")
]
