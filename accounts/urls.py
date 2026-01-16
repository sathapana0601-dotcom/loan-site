from django.urls import path
from . import views

urlpatterns = [
    path("", views.choose_view, name="choose"),
    path("choose/", views.choose_view, name="choose2"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
]
