from django.db.models import Q
from django.views.generic import DetailView, ListView, TemplateView
from .models import Category, Dish


class HomeView(TemplateView):
  template_name = "menu/home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["popular_dishes"] = Dish.objects.filter(is_available=True)[:6]
    context["new_dishes"] = Dish.objects.filter(is_available=True).order_by(
        "-created_at"
    )[:4]
    return context


class DishListView(ListView):
  model = Dish
  template_name = "menu/dish_list.html"
  context_object_name = "dishes"

  def get_queryset(self):
    queryset = Dish.objects.filter(is_available=True)
    category_slug = self.request.GET.get("category")
    query = self.request.GET.get("q")

    if category_slug:
      queryset = queryset.filter(category__slug=category_slug)

    if query:
      queryset = queryset.filter(
          Q(name__icontains=query) | Q(description__icontains=query)
      )

    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categories"] = Category.objects.all()
    context["selected_category"] = self.request.GET.get("category")
    context["query"] = self.request.GET.get("q")
    return context


class DishDetailView(DetailView):
  model = Dish
  template_name = "menu/dish_detail.html"
  context_object_name = "dish"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    dish = self.get_object()
    context["reviews"] = (
        dish.reviews.filter(is_approved=True) if hasattr(dish, "reviews") else []
    )
    return context