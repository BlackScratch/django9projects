from django.db import models
# https://docs.djangoproject.com/en/5.0/ref/models/fields/
# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    order_name = models.CharField(max_length=200, verbose_name='Заказчик')
    order_phone = models.CharField(max_length=200, verbose_name='телефон')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

# После этого пересобираем файл миграции  python manage.py makemigrations
# После этого применяем миграцию  python manage.py migrate