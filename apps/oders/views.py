from django.shortcuts import render


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.carts.models import Cart
from .forms import OrderForm
from .models import Order
from .services import create_order_from_cart

@login_required
def order_create_view(request):
    """Оформление заказа из корзины."""
    cart = Cart.objects.get_or_create(user=request.user)[0]
    if not cart.items.exists():
        messages.warning(request, 'Корзина пуста — нечего оформлять.')
        return redirect('carts:detail')
    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():
            order = create_order_from_cart(cart, **form.cleaned_data)
            messages.success(request, f'Заказ No{order.pk} принят!')
            return redirect('orders:detail', pk=order.pk)
    else:
    # Предзаполняем из профиля
        initial = {
        'address': request.user.profile.address,
        'phone': request.user.profile.phone,
        }
        form = OrderForm(initial=initial)
    return render(request, 'orders/order_form.html', {
    'form': form,
    'cart': cart,
    })