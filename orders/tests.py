'''
package: orders
description: tests
'''
from decimal import Decimal
from django.test import TestCase
from . import models


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


    def test_order_save(self):
        '''
        test for order model's save method
        '''
        self.assertEqual(self.order.number,
                '2020-01-15 Заказ:1')

    def test_order_price(self):
        '''
        test for order model's price method
        '''
        self.assertEqual(self.order.price(), Decimal('50'))
    """
    def test_orderitem_str(self):
        '''
        test for OrderItem model's __str__ method
        '''
        self.assertEqual(self.order_item.__str__(), 'Товар: Кирпич(5) цена: 50.00')
    """
    def test_orderitem_save(self):
        '''
        test for OrderItem models save method
        '''
        self.assertEqual(self.order_item.price, Decimal('50.00'))

