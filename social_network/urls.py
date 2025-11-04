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
    path('like/<int:post_id>/', views.like, name="like"),
    path('diss_like/<int:post_id>/', views.diss_like, name="diss_like"),
    path('comment/<int:post_id>/', views.comment, name="comment"),
    path('comment_like/<int:comment_id>/<int:post_id>/', views.comment_like, name="comment_like"),
    path("change_profile/<int:user_id>/", views.change_profile, name = "change_profile"),
    path("community_create_page/", views.community_create_view, name="community_create"),
    path("communities/", views.communities, name="communities"),
    path("community_info/<int:community_id>/", views.community_info, name="community_info"),
    path("diskussion/<int:community_id>/", views.diskussion, name="diskussion"),
    path("notification/", views.notification_view, name="notification"),
]
