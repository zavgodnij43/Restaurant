from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from .forms import OrderCreateForm
from .models import Order, OrderItem


class OrderCreateView(View):
  template_name = 'orders/checkout.html'

  def get(self, request, *args, **kwargs):
    cart = Cart(request)
    if len(cart) == 0:
      messages.warning(request, 'Ваш кошик порожній!')
      return redirect('cart_detail')

    form = OrderCreateForm()
    if request.user.is_authenticated:
      form.initial['full_name'] = (
          f'{request.user.first_name} {request.user.last_name}'.strip()
      )
      if hasattr(request.user, 'profile'):
        form.initial['phone'] = request.user.profile.phone
        form.initial['address'] = request.user.profile.address

    return render(request, self.template_name, {'form': form, 'cart': cart})

  def post(self, request, *args, **kwargs):
    cart = Cart(request)
    if len(cart) == 0:
      messages.warning(request, 'Ваш кошик порожній!')
      return redirect('cart_detail')

    form = OrderCreateForm(request.POST)
    if form.is_valid():
      order = form.save(commit=False)
      if request.user.is_authenticated:
        order.user = request.user
      order.total_price = cart.get_total_price()
      order.save()

      for item in cart:
        OrderItem.objects.create(
            order=order,
            dish=item['dish'],
            quantity=item['quantity'],
            price=item['price'],
        )

      cart.clear()
      messages.success(request, f'Замовлення #{order.id} успішно оформлено!')
      return redirect('order_detail', pk=order.pk)

    return render(request, self.template_name, {'form': form, 'cart': cart})


class OrderListView(LoginRequiredMixin, ListView):
  model = Order
  template_name = 'orders/order_history.html'
  context_object_name = 'orders'

  def get_queryset(self):
    return Order.objects.filter(user=self.request.user).order_by('-created_at')


class OrderDetailView(LoginRequiredMixin, DetailView):
  model = Order
  template_name = 'orders/order_detail.html'
  context_object_name = 'order'

  def get_queryset(self):
    if self.request.user.is_staff:
      return Order.objects.all()
    return Order.objects.filter(user=self.request.user)


class RepeatOrderView(LoginRequiredMixin, View):

  def get(self, request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    cart = Cart(request)
    for item in order.items.all():
      if item.dish and item.dish.is_available:
        cart.add(dish=item.dish, quantity=item.quantity, update_quantity=False)
    messages.success(
        request, f'Страви із замовлення #{order.id} додано до кошика!'
    )
    return redirect('cart_detail')