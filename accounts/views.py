from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(CreateView):
  form_class = UserRegisterForm
  template_name = "accounts/register.html"
  success_url = reverse_lazy("login")

  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(form.cleaned_data["password"])
    user.save()
    messages.success(
        self.request, "Акаунт успішно створено! Тепер ви можете увійти."
    )
    return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):
  template_name = "accounts/profile.html"

  def get(self, request, *args, **kwargs):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST, instance=request.user.profile
    )

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, "Ваш профіль успішно оновлено!")
      return redirect("profile")

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, self.template_name, context)