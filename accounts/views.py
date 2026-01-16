from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


def choose_view(request):
    return render(request, "choose.html")


def login_view(request):
    if request.method == "POST":
        phone = (request.POST.get("phone") or "").strip()
        password = request.POST.get("password") or ""

        user = authenticate(request, username=phone, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Incorrect phone number or password. Please try again.")
        return redirect("login")

    return render(request, "login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        phone = (request.POST.get("phone") or "").strip()
        password = request.POST.get("password") or ""
        confirm = request.POST.get("confirm_password") or ""

        # ✅ hidden input from register.html
        agreed = (request.POST.get("agree_accepted") == "1")

        if not phone:
            messages.error(request, "Phone number is required.")
            return redirect("register")

        if User.objects.filter(phone=phone).exists():
            messages.error(request, "This phone number is already registered. Please log in instead.")
            return redirect("register")

        if not password:
            messages.error(request, "Password is required.")
            return redirect("register")

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if not agreed:
            messages.error(request, "Please read and agree before click Register.")
            return redirect("register")

        user = User.objects.create_user(phone=phone, password=password)
        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("dashboard")

    return render(request, "register.html")


@login_required(login_url="/login/")
def dashboard_view(request):
    return render(request, "dashboard.html")


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, "profile.html")


def logout_view(request):
    logout(request)
    return redirect("login")
