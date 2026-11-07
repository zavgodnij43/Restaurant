from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.OrderCreateView.as_view(), name='checkout'),
    path('history/', views.OrderListView.as_view(), name='order_history'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('repeat/<int:pk>/', views.RepeatOrderView.as_view(), name='repeat_order'),
]