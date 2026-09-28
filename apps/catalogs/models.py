from django.db import models


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название',)

    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-идентификатор',)

    is_active = models.BooleanField(default=True,verbose_name='Активна',)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name='dishes',
    verbose_name='Категория',
    )

    name = models.CharField(max_length=200, verbose_name='Название',)

    slug = models.SlugField(max_length=200,unique=True, verbose_name='URL-идентификатор',)

    description = models.TextField(blank=True, verbose_name='Описание',)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',)
    
    image = models.ImageField(
        upload_to='dishes/',
        blank=True,
        null=True,
        verbose_name='Фото',)
    
    is_available = models.BooleanField(default=True,verbose_name='Доступно',)

    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name='Создано',)
    updated_at = models.DateTimeField(
        auto_now=True,verbose_name='Обновлено',)
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['name']
        indexes = [models.Index(fields=['slug']),]
    def __str__(self):
        return self.name

