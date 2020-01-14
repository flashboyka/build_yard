from django.db import models

from uuid import uuid4
from datetime import date

from contragents.models import Contragent
from goods.models import Good


class Order(models.Model):
    number = models.CharField(max_length=25, blank=True, editable=False, verbose_name = 'Номер заказа')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')
    edited = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата изменения')
    counteragent = models.ForeignKey(Contragent, on_delete=models.CASCADE, verbose_name='Контрагент')

    def __str__(self):
        return self.number

    def price(self):
        return self.orderitem_set.aggregate(models.Sum('price')).get('price__sum')

    def save(self, *args, **kwargs):
        self.number = '{0} Заказ:{1}'.format(date.today(), Order.objects.filter(created__date=date.today()).count() + 1)
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, verbose_name='Цена')

    def __str__(self):
        return f'Товар: {self.good.name}({self.count}) цена: {self.price}'

    def save(self, *args, **kwargs):
        self.price = self.good.price * self.count
        super(OrderItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар в заказа'
        verbose_name_plural = 'Перечень заказа'
