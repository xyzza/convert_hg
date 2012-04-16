#coding:utf-8
from django.db import models

class PublicCatering(models.Model):
    '''
    Класс, описывающий заведение общественного питания.
    '''
    # Наименование общепита.
    name = models.CharField(max_length=100, default=u'')

    class Meta:
        db_table = 'public_catering'
        verbose_name = u'Общепит'