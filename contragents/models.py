from django.db import models


class Contragent(models.Model):
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    middle_name = models.CharField(max_length=25, verbose_name='Отчество')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Контрагента'
        verbose_name_plural = 'Контрагенты'
