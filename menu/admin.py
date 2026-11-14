from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
  prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'price', 'available', 'created_at')
  list_filter = ('available', 'category')
  search_fields = ('name', 'description')
  list_editable = ('price', 'available')