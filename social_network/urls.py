from django.urls import path
from . import views
from .views import profile_view
from authenticator.views import login_view, register_view, logout_view

app_name = "sn"

urlpatterns = [
    path("", views.home_view, name = "home"),
    path('profile/', profile_view, name='profile'),
]

