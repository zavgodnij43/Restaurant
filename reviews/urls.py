from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:dish_id>/', views.AddReviewView.as_view(), name='add_review'),
]