'''
package: contragent
description: tests
'''
from django.test import TestCase, Client
from . import models

class ContragentTestCase(TestCase):
    '''
    tests for contragent application
    '''
    fixtures = ['fixture_contragent.json']

    def setUp(self):
        '''
        defining required data
        '''
        self.contragent = models.Contragent.objects.last()


    def test_contragent_str(self):
        '''
        test for contragent model's __str__ method
        '''
        self.assertEqual(self.contragent.__str__(), 'Иванов Иван Иванович')
