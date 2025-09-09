from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .forms import CreatePost, Filter
from .admin import PostAdmin
from .models import Subscribe, Friendship, Post, Like, Diss_like, Comment, Like_comment
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

def change_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "sn/change_profile.html", {"profile": user.profile})

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
def like(request, post_id):
    obj, created = Like.objects.get_or_create(post_follower_id=request.user.id, post_id=post_id)
    if not created:
        obj.delete()
    return redirect("sn:post_info", post_id)

@login_required
def diss_like(request, post_id):
    obj, created = Diss_like.objects.get_or_create(post_follower_id=request.user.id, post_id=post_id)
    if not created:
        obj.delete()
    return redirect("sn:post_info", post_id)

@login_required
def comment(request, post_id):
    if request.method == 'POST':
        obj = Comment.objects.create(comment_maker=request.user, post_id=post_id, text=request.POST['comment_text'])
    return redirect("sn:post_info", post_id)

@login_required
def comment_like(request, comment_id, post_id):
    obj, created = Like_comment.objects.get_or_create(comment_follower_id=request.user.id, comment_id=comment_id)
    if not created:
        obj.delete()
    return redirect("sn:post_info", post_id)


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
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Пост успешно создан")
            return redirect("sn:home")

    return render(request, "sn/create_post.html", {"form": form})

def posts(request):
    posts = Post.objects.filter(status='published')
    form = Filter(request.GET)
    author = request.GET.get("author")
    created = request.GET.get("created")
    print(created)
    date1 = request.GET.get("date1")
    date2 = request.GET.get("date2")
    if author:
        posts = posts.filter(author__username=author)
    if created:
        posts = posts.filter(created__date=created)
    if date1:
        posts = posts.filter(created__date__lt=date2)
    if date2:
        posts = posts.filter(created__date__gt=date1)

    return render(request, "sn/posts_page.html", {"posts": posts, "form": form})


@login_required
def post_info(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, "sn/post_info.html", {"post": post, "comments": post.comments.all()})


