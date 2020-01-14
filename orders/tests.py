'''
package: orders
description: tests
'''
import datetime
import decimal
from django.db import models as django_models
from django.test import TestCase, Client
from . import models


class OrderTestCase(TestCase):
    '''
    tests for orders application
    '''
    def setUp(self) -> None:
        '''
        setUp method, for defining required data
        '''
        self.client = Client()
        self.client.login(username='admin', password='123654atm')
        self.today = datetime.datetime.today()
        self.contragent = models.Contragent.objects.create(
            last_name='Иванов',
            first_name='Иван',
            middle_name='Иванович',
            email='iii@mail.ru',
            phone='5555555',
            address='ул. Строителей, д. 5, кв. 21'
        )
        self.good = models.Good.objects.create(
            name='Кирпич',
            price=decimal.Decimal(10)
        )
        self.order = models.Order.objects.create(
            contragent=self.contragent
        )
        self.order_item = models.OrderItem.objects.create(
            order=self.order,
            good=self.good,
            count=10
        )


    def test_order_save(self):
        '''
        test for order model's save method
        '''
        self.assertEqual(self.order.number,
                f'{datetime.date.isoformat(self.today)} Заказ:{models.Order.objects.filter(created__date=self.today.date()).count()+1}')

    def test_order_price(self):
        '''
        test for order model's price method
        '''
        self.assertEqual(self.order.price(), self.order.orderitem_set.aggregate(django_models.Sum('price')).get('price__sum'))

    def test_orderitem_str(self):
        '''
        test for OrderItem model's __str__ method
        '''
        self.assertEqual(self.order_item.__str__(), f'Товар: {self.order_item.good.name}({self.order_item.count}) цена: {self.order_item.price}')

    def test_orderitem_save(self):
        '''
        test for OrderItem models save method
        '''
        self.assertEqual(self.order_item.price, self.order_item.good.price * self.order_item.count)

