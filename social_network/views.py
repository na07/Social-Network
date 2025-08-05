from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .forms import CreatePost
from .admin import PostAdmin
from .models import Subscribe, Friendship, Post
from django.contrib.auth.models import User
from authenticator.models import Profile
from django.contrib import messages


# Create your views here.

@login_required
def friends_request_view(request):
    requests = Friendship.objects.filter(friend=request.user, confirmed=False)
    return render(request, "sn/friends_request_page.html", {"requests": requests})


def home_view(request):
    return render(request, "sn/home_page.html")


@login_required
def profile_view(request: HttpRequest, user_id: int) -> HttpResponse:
    user = get_object_or_404(User, id=user_id)
    friends = Friendship.objects.filter(Q(user=user) | Q(friend=user), confirmed=True)
    posts = Post.objects.filter(author=user, status='published')
    return render(request, "sn/profile_page.html", {"profile": user.profile, "friends": friends, "posts": posts})

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


@login_required
def accept_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id)

    if friendship.friend != request.user:
        return redirect('sn:friends_requests')

    friendship.confirmed = True
    friendship.save()


    return redirect('sn:friends_requests')


@login_required
def decline_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id)

    if friendship.friend != request.user:
        return redirect('sn:friends_requests')

    friendship.delete()
    return redirect('sn:friends_requests')

@login_required
def delete_friend(request, friend_id):
    friendship = get_object_or_404(Friendship, id=friend_id)

    friendship.delete()

    return redirect('sn:profile', user_id=request.user.id)


@login_required
def create_post(request):
    form = CreatePost()
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Пост успешно создан")
            return redirect("sn:home")

    return render(request, "sn/create_post.html", {"form": form})


def posts(request):
    posts = Post.objects.filter(status='published')
    return render(request, "sn/posts_page.html", {"posts": posts})


def post_info(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, "sn/post_info.html", {"post": post})


