from django.urls import path
from .views import classify_sneaker

name = "sneakers_image_recog"

urlpatterns = [
    path("classifier/", classify_sneaker, name="img_classify")
]
