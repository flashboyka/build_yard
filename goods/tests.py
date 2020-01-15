'''
package: tests
description: goods
'''
from django.test import TestCase
from . import models

class GoodsTestCase(TestCase):
    '''
    tests for goods application
    '''
    fixtures = ['fixture_good.json']

    def setUp(self):
        '''
        method for defining required data
        '''
        self.good = models.Good.objects.last()

    def test_goods_str(self):
        '''
        test for Good model's __str__ method
        '''
        self.assertEqual(self.good.__str__(), 'Кирпич')

