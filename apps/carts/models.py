from django.db import models

from django.contrib.auth.models import User
from django.db import models
from apps.catalogs.models import Dish

class Cart(models.Model):
    """Корзина пользователя. Одна на пользователя."""
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='cart',
    verbose_name='Пользователь',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    def __str__(self):
        return f'Корзина {self.user.username}'
    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())
    
    @property
    def item_count(self):
        """Общее количество единиц товара."""
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    """Позиция корзины: блюдо + количество."""
    cart = models.ForeignKey(
    Cart,
    on_delete=models.CASCADE,
    related_name='items',
    verbose_name='Корзина',
    )
    dish = models.ForeignKey(
    Dish,
    on_delete=models.CASCADE,
    verbose_name='Блюдо',
    )
    quantity = models.PositiveIntegerField(
    default=1,
    verbose_name='Количество',
    )
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Позиция корзины'
        verbose_name_plural = 'Позиции корзины'
        unique_together = ('cart', 'dish') # одно блюдо — одна строка
        ordering = ['-added_at']
    def __str__(self):
        return f'{self.dish.name} × {self.quantity}'
    @property
    def subtotal(self):
        """Стоимость позиции."""
        return self.dish.price * self.quantity    