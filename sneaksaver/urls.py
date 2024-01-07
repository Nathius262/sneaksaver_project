from django.urls import path
from .views import index_view, product_detail_view, product_view, booking_view, pricing_view

urlpatterns = [
    path("", index_view, name="index"),
    path("product/", product_view, name="product"),
    path("product/detail/", product_detail_view, name="product_detail"),
    path("booking/", booking_view, name="booking"),
    path("pricing/", pricing_view, name="pricing"),
]
