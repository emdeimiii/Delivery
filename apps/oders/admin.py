from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('dish', 'dish_name', 'price', 'quantity')
    can_delete = False

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total', 'payment_method','is_paid', 'courier', 'created_at')
    list_filter = ('status', 'payment_method', 'is_paid', 'created_at')
    search_fields = ('user__username', 'phone', 'address', 'id')
    list_editable = ('status', 'is_paid', 'courier')
    list_select_related = ('user', 'courier')
    date_hierarchy = 'created_at'
    readonly_fields = ('user', 'total', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    fieldsets = (
    ('Основное', {
    'fields': ('user', 'status', 'total')
    }),
    ('Доставка', {
    'fields': ('address', 'phone', 'comment', 'courier')
    }),
    ('Оплата', {
    'fields': ('payment_method', 'is_paid')
    }),
    ('Служебное', {
    'fields': ('created_at', 'updated_at'),
    'classes': ('collapse',),
    }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish_name', 'price', 'quantity', 'subtotal')
    search_fields = ('dish_name', 'order__user__username')
    list_select_related = ('order', 'dish')
    def subtotal(self, obj):
        return f'{obj.subtotal} ₽'
    subtotal.short_description = 'Стоимость'
