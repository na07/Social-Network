from django.urls import path
from . import views
from .views import profile_view
from authenticator.views import login_view, register_view, logout_view


app_name = "sn"

urlpatterns = [
    path("", views.home_view, name = "home"),
    path("friends_request_page/", views.friends_request_view, name = "friends_requests"),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('subscribe/<int:user_id>/', views.subscribe, name='subscribe'),
    path('send_friend_request/<int:user_id>/', views.friend_ship, name='friendship'),
    path('accept_friend_request/<int:friendship_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:friendship_id>/', views.decline_friend_request, name='decline_friend_request'),
    path('delete_friend/<int:friend_id>/', views.delete_friend, name='delete_friend'),
    path("create_post/", views.create_post, name = "create_post"),
    path("posts/", views.posts, name = "posts"),
    path('post_info/<int:post_id>/', views.post_info, name='post_info'),
]

