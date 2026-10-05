from django.db import models

from django.contrib.auth.models import User
from django.db import models
from apps.accounts.models import Courier

class Order(models.Model):
    """Заказ пользователя."""
    STATUS_NEW = 'new'
    STATUS_ACCEPTED = 'accepted'
    STATUS_COOKING = 'cooking'
    STATUS_DELIVERING = 'delivering'
    STATUS_DONE = 'done'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (STATUS_NEW, 'Новый'),
        (STATUS_ACCEPTED, 'Принят'),
        (STATUS_COOKING, 'Готовится'),
        (STATUS_DELIVERING, 'В доставке'),
        (STATUS_DONE, 'Доставлен'),

        (STATUS_CANCELLED, 'Отменён'),
    ]

    PAYMENT_CASH = 'cash'
    PAYMENT_CARD = 'card'

    PAYMENT_CHOICES = [
        (PAYMENT_CASH, 'Наличными курьеру'),
        (PAYMENT_CARD, 'Картой курьеру'),
    ]
    user = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    related_name='orders',
    verbose_name='Пользователь',
    )
    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default=STATUS_NEW,
    verbose_name='Статус',
    )
    # Контактные данные — копируем, а не берём из профиля
    address = models.CharField(max_length=300, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default=PAYMENT_CASH,
        verbose_name='Способ оплаты',
    )
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')
    # Логистика
    courier = models.ForeignKey(
    Courier,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='orders',
    verbose_name='Курьер',
    )
    # Итог — фиксируется при создании
    total = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    verbose_name='Сумма',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
    def __str__(self):
        return f'Заказ No{self.pk} от {self.user.username}'
    def can_be_cancelled(self):
        """Отменить можно только новый или принятый."""
        return self.status in (self.STATUS_NEW, self.STATUS_ACCEPTED)

class OrderItem(models.Model):
    """Позиция заказа. Хранит копию цены и названия."""
    order = models.ForeignKey(
    Order,
    on_delete=models.CASCADE,
    related_name='items',
    verbose_name='Заказ',
    )
    dish = models.ForeignKey(
    'catalog.Dish',
    on_delete=models.PROTECT,
    verbose_name='Блюдо',
    )

    dish_name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(
    max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
    def __str__(self):
        return f'{self.dish_name} × {self.quantity}'
    @property
    def subtotal(self):
        return self.price * self.quantity