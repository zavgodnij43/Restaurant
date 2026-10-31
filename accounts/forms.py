from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
  password_confirm = forms.CharField(
      widget=forms.PasswordInput, label="Підтвердження пароля"
  )

  class Meta:
    model = User
    fields = ["username", "email"]

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    password_confirm = cleaned_data.get("password_confirm")
    if password and password_confirm and password != password_confirm:
      raise forms.ValidationError("Паролі не співпадають!")
    return cleaned_data


class UserUpdateForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ["username", "email", "first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ["phone", "address"]