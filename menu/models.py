from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=100, unique=True, verbose_name='Назва')
  slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')

  class Meta:
    verbose_name = 'Категорія'
    verbose_name_plural = 'Категорії'
    ordering = ['name']

  def __str__(self):
    return self.name


class Dish(models.Model):
  name = models.CharField(max_length=200, verbose_name='Назва страви')
  category = models.ForeignKey(
      Category,
      on_delete=models.CASCADE,
      related_name='dishes',
      verbose_name='Категорія',
  )
  description = models.TextField(verbose_name='Опис')
  price = models.DecimalField(
      max_digits=8, decimal_places=2, verbose_name='Ціна'
  )
  image = models.ImageField(
      upload_to='dishes/', blank=True, null=True, verbose_name='Зображення'
  )
  available = models.BooleanField(default=True, verbose_name='В наявності')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

  class Meta:
    verbose_name = 'Страва'
    verbose_name_plural = 'Страви'
    ordering = ['name']

  def __str__(self):
    return self.name