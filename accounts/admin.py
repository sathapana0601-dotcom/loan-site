from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ("-date_joined",)
    list_display = ("phone", "balance", "status", "is_staff", "is_active")
    list_filter = ("status", "is_staff", "is_active")
    search_fields = ("phone",)

    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Wallet / Status", {"fields": ("balance", "status")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    # Remove username/email fields from default DjangoUserAdmin
    username_field = "phone"
