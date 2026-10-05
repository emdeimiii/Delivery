from decimal import Decimal
from django.db import transaction
from apps.carts.models import Cart
from .models import Order, OrderItem

@transaction.atomic
def create_order_from_cart(cart: Cart, **order_data) -> Order:
    """Создаёт заказ из корзины. Атомарно.
    order_data — поля Order: address, phone, comment, payment_method.
    """
    order = Order.objects.create(
    user=cart.user,
    total=Decimal('0'),
    **order_data,
    )

    total = Decimal('0')
    for cart_item in cart.items.select_related('dish').all():
        OrderItem.objects.create(
            order=order,
            dish=cart_item.dish,
            dish_name=cart_item.dish.name, # снапшот
            price=cart_item.dish.price, # снапшот
            quantity=cart_item.quantity,
        )
        total += cart_item.dish.price * cart_item.quantity
    order.total = total
    order.save(update_fields=['total'])
    cart.items.all().delete()
    return order