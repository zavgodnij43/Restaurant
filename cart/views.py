from cart.cart import Cart
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from menu.models import Dish


class CartDetailView(View):

  def get(self, request, *args, **kwargs):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})


class CartAddView(View):

  def post(self, request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    quantity = int(request.POST.get("quantity", 1))
    update = request.POST.get("update", False)
    cart.add(dish=dish, quantity=quantity, update_quantity=update)
    return redirect("cart_detail")


class CartRemoveView(View):

  def post(self, request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish)
    return redirect("cart_detail")