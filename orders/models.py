from django.contrib.auth.models import User
from django.db import models
from menu.models import Dish


class Order(models.Model):
  PAYMENT_CHOICES = (
      ('cash', 'Готівкою при отриманні'),
      ('card', 'Карткою онлайн'),
  )

  STATUS_CHOICES = (
      ('pending', 'Очікує на підтвердження'),
      ('preparing', 'Готується'),
      ('delivering', 'Доставляється'),
      ('completed', 'Виконано'),
      ('cancelled', 'Скасовано'),
  )

  user = models.ForeignKey(
      User,
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      verbose_name='Користувач',
  )
  full_name = models.CharField(max_length=100, verbose_name="Повне ім'я")
  phone = models.CharField(max_length=20, verbose_name='Телефон')
  address = models.TextField(verbose_name='Адреса доставки')
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name='Дата замовлення'
  )
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
  status = models.CharField(
      max_length=20,
      choices=STATUS_CHOICES,
      default='pending',
      verbose_name='Статус',
  )
  payment_method = models.CharField(
      max_length=20,
      choices=PAYMENT_CHOICES,
      default='cash',
      verbose_name='Спосіб оплати',
  )
  total_price = models.DecimalField(
      max_digits=10, decimal_places=2, verbose_name='Загальна сума'
  )

  def __str__(self):
    return f'Замовлення #{self.id} ({self.full_name})'


class OrderItem(models.Model):
  order = models.ForeignKey(
      Order,
      related_name='items',
      on_delete=models.CASCADE,
      verbose_name='Замовлення',
  )
  dish = models.ForeignKey(
      Dish, on_delete=models.SET_NULL, null=True, verbose_name='Страва'
  )
  price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
  quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')

  def __str__(self):
    return f"{self.quantity} x {self.dish.name if self.dish else 'Видалена страва'}"