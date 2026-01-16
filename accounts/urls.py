from django.urls import path
from . import views

urlpatterns = [
    path("choose/", views.choose_view, name="choose"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),

    # new pages
    path("credit-score/", views.credit_score_view, name="credit_score"),
    path("loan-apply/", views.loan_apply_view, name="loan_apply"),
    path("transactions/", views.transactions_view, name="transactions"),
    path("payment-schedule/", views.payment_schedule_view, name="payment_schedule"),

    path("logout/", views.logout_view, name="logout"),
]
