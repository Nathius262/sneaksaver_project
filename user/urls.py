from django.urls import path
from .views import account_setting_view

app_name="user"

urlpatterns = [
    path("settings/", account_setting_view, name="account_settings")
]