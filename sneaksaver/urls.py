from django.urls import path
from .views import (
    index_view, DetailPostView, product_view, 
    booking_view, pricing_view, about_page_view,
    contact_view,
    message_agent_view,
)

urlpatterns = [
    path("", index_view, name="index"),
    path("product/", product_view, name="product"),
    path("product/<str:slug>/detail/", DetailPostView.as_view(), name="product_detail"),
    path("booking/", booking_view, name="booking"),
    path("pricing/", pricing_view, name="pricing"),
    path("about/", about_page_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("message/", message_agent_view, name="message_agent"),
]
