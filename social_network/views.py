from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from authenticator.models import Profile


# Create your views here.

def home_view(request):
    return render(request, "sn/home_page.html")

@login_required
def profile_view(request:HttpRequest) -> HttpResponse:
    authents = Profile.objects.filter(owner=request.user)
    return render(request, "sn/profile_page.html", {"profile": authents.first()})