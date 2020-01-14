'''
package: tests
description: goods
'''
from django.test import TestCase
from django.test import Client
from . import models

class GoodsTestCase(TestCase):
    '''
    tests for goods application
    '''
    def setUp(self) -> None:
        '''
        method for defining required data
        '''
        self.client = Client()
        self.client.login(username='admin', password='123654atm')
        self.good = models.Good.objects.create(
            name='Кирпич',
            price='10'
        )

    def test_goods_str(self):
        '''
        test for Good model's __str__ method
        '''
        self.assertEqual(self.good.__str__(), 'Кирпич')

