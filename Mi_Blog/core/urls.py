from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import *

urlpatterns = [
    path("", home, name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/nuevo/", post_create, name="post_create"),
    path("post/<int:pk>/editar/", post_edit, name="post_edit"),
    path("registro/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]
