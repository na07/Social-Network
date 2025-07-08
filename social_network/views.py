from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Subscribe, Friendship
from django.contrib.auth.models import User
from authenticator.models import Profile


# Create your views here.

def friends_request_view(request):
    #тут дз
    return render(request, "sn/friends_request_page.html")

def home_view(request):
    return render(request, "sn/home_page.html")

@login_required
def profile_view(request: HttpRequest, user_id: int) -> HttpResponse:
    user = get_object_or_404(User, id=user_id)
    return render(request, "sn/profile_page.html", {"profile": user.profile})

@login_required
def subscribe(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    obj, created = Subscribe.objects.get_or_create(follower=request.user, user=user_to_follow)
    if not created:
        obj.delete()
    return redirect("sn:profile", user_id)

@login_required
def friend_ship(request, user_id):
    user_to_friend_add = get_object_or_404(User, id=user_id)
    obj, created = Friendship.objects.get_or_create(user=request.user, friend=user_to_friend_add)
    if not created:
        obj.delete()
    return  redirect("sn:profile", user_id)
