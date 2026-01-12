from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("bot/", views.BotView.as_view(), name="bot"),
    path("local/", views.ProfileView.as_view(), name="profile"),
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True,
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="accounts/logout.html",
    ), name="logout"),
]