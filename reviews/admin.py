from django.contrib import admin
from .models import Review  # Імпортуємо Review з поточного додатку


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = ('dish', 'user', 'rating', 'is_approved', 'created_at')
  list_filter = ('is_approved', 'rating', 'created_at')
  list_editable = ('is_approved',)
  search_fields = ('text', 'user__username', 'dish__name')