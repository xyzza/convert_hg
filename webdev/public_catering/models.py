#coding:utf-8
from datetime import time
from django.db import models

class PublicCatering(models.Model):
    '''
    Класс, описывающий заведение общественного питания.
    '''
    # Наименование общепита.
    name = models.CharField(u'наименование', max_length=100, default=u'')
    # Телефон
    phone = models.CharField(u'телефон', max_length=20, blank=True, default=u'')
    # Адрес
    address = models.CharField(u'адрес', max_length=100, blank=True, default=u'')
    # Сайт
    site = models.URLField(u'сайт', blank=True, default=u'')
    # Формат заведения
#    format = models.SmallIntegerField()
    # Описание общепита
    description = models.TextField(u'описание', max_length=1000, blank=True, default='')
    # Долгота
#    longitude = models.DecimalField(u'долгота')
#    # Широта
#    latitude = models.DecimalField(u'широта')
    # Время открытия
    time_opening = models.TimeField(u'время открытия', auto_now=False, auto_now_add=False, default=time(10,0))
    # Время закрытия
    time_closed = models.TimeField(u'время закрытия', auto_now=False, auto_now_add=False, default=time(22,0))
    # Минимальная стоимость заказа
    min_price = models.DecimalField(u'минимальная стоимость', max_digits=16, decimal_places=2, blank=True, default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'public_catering'
        verbose_name = u'Общепит'