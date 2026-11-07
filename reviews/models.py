from django.contrib.auth.models import User
from django.db import models
from menu.models import Dish


class Review(models.Model):
  dish = models.ForeignKey(
      Dish,
      on_delete=models.CASCADE,
      related_name="reviews",
      verbose_name="Страва",
  )
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, verbose_name="Користувач"
  )
  rating = models.PositiveIntegerField(verbose_name="Оцінка (1-5)")
  text = models.TextField(verbose_name="Текст відгуку")
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name="Дата відгуку"
  )
  is_approved = models.BooleanField(
      default=False, verbose_name="Схвалено адміністратором"
  )

  def __str__(self):
    return f"Відгук від {self.user.username} на {self.dish.name}"