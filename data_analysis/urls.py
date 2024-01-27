from django.urls import path
from .views import search_view, faq_views

name = "data_analysis"

urlpatterns = [
    path('search/', search_view, name="search"),
    path("faqs/", faq_views, name="faq"),
]
