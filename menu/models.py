from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name="Категорія")
  slug = models.SlugField(unique=True, verbose_name="Слаг")

  def __str__(self):
    return self.name


class Dish(models.Model):
  category = models.ForeignKey(
      Category,
      on_delete=models.CASCADE,
      related_name="dishes",
      verbose_name="Категорія",
  )
  name = models.CharField(max_length=150, verbose_name="Назва страви")
  description = models.TextField(verbose_name="Опис")
  ingredients = models.TextField(verbose_name="Інгредієнти")
  price = models.DecimalField(
      max_digits=8, decimal_places=2, verbose_name="Ціна"
  )
  image = models.ImageField(
      upload_to="dishes/", blank=True, null=True, verbose_name="Фото"
  )
  is_available = models.BooleanField(
      default=True, verbose_name="В наявності"
  )
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name="Дата створення"
  )

  def __str__(self):
    return self.name