'''
package: orders
description: tests
'''
import datetime
from decimal import Decimal
from django.test import TestCase
from . import models
from goods import models as good_models


class OrderTestCase(TestCase):
    '''
    tests for orders application
    '''
    fixtures = ['fixture_order.json']

    def setUp(self):
        '''
        setUp method, for defining required data
        '''
        self.order = models.Order.objects.last()
        self.order_item = self.order.orderitem_set.last()

    def test_order_str(self):
        self.assertIs(self.order.__str__(), self.order.number)

    def test_order_save(self):
        '''
        test for order model's save method
        '''
        today = datetime.date.today()
        new_order = models.Order.objects.create(
            contragent = models.Contragent.objects.last()
        )
        new_order.save()
        order = models.Order.objects.last()
        self.assertEqual(order.number, f'{today} Заказ:{models.Order.objects.filter(created__date=today).count()+1}')

    def test_order_price(self):
        '''
        test for order model's price method
        '''
        self.assertEqual(self.order.price(), Decimal('50'))

    def test_order_str(self):
        self.assertEqual(self.order.__str__(), self.order.number)

    def test_orderitem_str(self):
        '''
        test for OrderItem model's __str__ method
        '''
        self.assertEqual(self.order_item.__str__(), 'Товар: Кирпич(5) цена: 50.00')

    def test_orderitem_save(self):
        '''
        test for OrderItem models save method
        '''
        order_item = models.OrderItem.objects.create(
            order = models.Order.objects.last(),
            good = good_models.Good.objects.last(),
            count = 5
        )
        order_item.save()
        self.assertEqual(order_item.price, order_item.good.price*order_item.count)

