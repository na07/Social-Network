from django.urls import path
from . import views
from .views import profile_view
from authenticator.views import login_view, register_view, logout_view


app_name = "sn"

urlpatterns = [
    path("", views.home_view, name = "home"),
    path("friends_request_page/", views.friends_request_view, name = "friends_request"),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('subscribe/<int:user_id>/', views.subscribe, name='subscribe'),
    path('friendship/<int:user_id>/', views.friend_ship, name="friendship")
]

