from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='profile',
    verbose_name='Пользователь',)

    phone = models.CharField(
    max_length=20,
    blank=True,
    verbose_name='Телефон',)

    address = models.CharField(
    max_length=300,
    blank=True,
    verbose_name='Адрес доставки',)

    birth_date = models.DateField(
    null=True,
    blank=True,
    verbose_name='Дата рождения',)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    def __str__(self):
        return f'Профиль {self.user.username}'


# class Profile(models.Model):
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE,
#         retated_name = 'profile',
#     )
#     name = models.CharField(max_length=60, )
#     last_name= models.CharField(max_length=60,)
#     address = models.TextField()