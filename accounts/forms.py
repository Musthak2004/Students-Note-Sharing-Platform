from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")

    def clean_role(self):
        role = self.cleaned_data.get("role")
        if role not in ["student", "teacher", "admin"]:
            raise forms.ValidationError("Invalid role.")
        return role

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")