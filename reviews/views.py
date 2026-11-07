from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from menu.models import Dish
from .forms import ReviewForm


class AddReviewView(LoginRequiredMixin, View):

  def post(self, request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.user = request.user
      review.dish = dish
      review.save()
      messages.success(
          request,
          "Ваш відгук успішно надіслано та він з'явиться після модерації!",
      )
    else:
      messages.error(
          request, "Помилка при додаванні відгуку. Перевірте правильність полів."
      )
    return redirect("dish_detail", pk=dish.pk)