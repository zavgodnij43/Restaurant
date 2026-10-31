from django.urls import path
from . import views

urlpatterns = [
    path("", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:dish_id>/", views.CartAddView.as_view(), name="cart_add"),
    path(
        "remove/<int:dish_id>/",
        views.CartRemoveView.as_view(),
        name="cart_remove",
    ),
]