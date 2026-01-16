from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=6)

    class Meta:
        model = User
        fields = ["phone"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if not phone.isdigit():
            raise forms.ValidationError("Phone must be digits only.")
        return phone

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Passwords do not match.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        # ងាយៗ៖ ប្រើ username = phone ដើម្បី login ដោយ phone
        user.username = self.cleaned_data["phone"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user