#coding:utf-8
from public_catering.models import PublicCatering
from django.contrib import admin

class PublicCateringAdmin(admin.ModelAdmin):
    '''
    Модель описывает форму редактирования общепита.
    '''
    fields = ['name', 'phone', 'address', 'site',
              'description', 'min_price', 'time_opening', 'time_closed']

# выполним регистрацию общепитов в регистраторской:
admin.site.register(PublicCatering, PublicCateringAdmin)

