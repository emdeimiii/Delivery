from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Courier

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'

class CourierInline(admin.StackedInline):
    model = Courier
    can_delete = True
    verbose_name_plural = 'Курьер'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, CourierInline)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_courier')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    def is_courier(self, obj):
        return hasattr(obj, 'courier')
    is_courier.boolean = True
    is_courier.short_description = 'Курьер'

# Перерегистрируем стандартную админку User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date')
    search_fields = ('user__username', 'user__email', 'phone')
    list_select_related = ('user',)

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'transport', 'is_active', 'hired_at')
    list_filter = ('is_active', 'transport')
    search_fields = ('user__username', 'user__first_name', 'phone')
    list_editable = ('is_active',)
    list_select_related = ('user',)