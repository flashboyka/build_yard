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

    def setUp(self) -> None:
        '''
        defining required data
        '''
        self.client = Client()
        self.client.login(username='admin', password='123654atm')
        self.contragent = models.Contragent.objects.create(
            last_name='Иванов',
            first_name='Иван',
            middle_name='Иванович',
            email='iii@mail.ru',
            phone='5555555',
            address='ул. Строителей, д. 25, кв. 12'
        )


    def test_contragent_str(self):
        '''
        test for contragent model's __str__ method
        '''
        self.assertEqual(self.contragent.__str__(), 'Иванов Иван Иванович')
