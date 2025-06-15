from django.urls import path
from . import views
from authenticator.views import login_view, register_view

app_name = "sn"

urlpatterns = [
    path("home_page/", views.home_page, name = "home"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]

