from django.urls import path
from . import views
from .views import profile_view
from authenticator.views import login_view, register_view, logout_view

app_name = "sn"

urlpatterns = [
    path("home_page/", views.home_view, name = "home"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='lg'),
]

