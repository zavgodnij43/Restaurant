from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('menu.urls')),  # Меню та головна сторінка в корені сайту
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
]

# Додаємо підтримку завантаження медіа-файлів (фото страв) у режимі розробки
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)