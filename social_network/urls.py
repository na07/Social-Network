from django.urls import path
from . import views

app_name = "sn"

urlpatterns = [
    path("", views.home_page, name = "home"),

]