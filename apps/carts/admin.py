from django.contrib import admin

from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('added_at',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_count', 'total', 'updated_at')
    search_fields = ('user__username', 'user__email')
    list_select_related = ('user',)
    inlines = [CartItemInline]
    def item_count(self, obj):
        return obj.item_count
    item_count.short_description = 'Позиций'
    def total(self, obj):
        return f'{obj.total} ₽'
    total.short_description = 'Сумма'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'dish', 'quantity', 'subtotal', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('dish__name', 'cart__user__username')
    list_select_related = ('cart', 'dish')
    def subtotal(self, obj):
        return f'{obj.subtotal} ₽'
    subtotal.short_description = 'Стоимость'
