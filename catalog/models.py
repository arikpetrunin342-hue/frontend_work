from django.db import models


class Category(models.Model):
    """Модель категории товара."""

    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель продукта."""

    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='products/')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )
    price = models.DecimalField('Цена за покупку', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего изменения', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
