from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("catalog/", views.DishListView.as_view(), name="dish_list"),
    path("dish/<int:pk>/", views.DishDetailView.as_view(), name="dish_detail"),
]