# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PublicCatering.min_price'
        db.add_column('public_catering', 'min_price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=2, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'PublicCatering.min_price'
        db.delete_column('public_catering', 'min_price')

    models = {
        'public_catering.publiccatering': {
            'Meta': {'object_name': 'PublicCatering', 'db_table': "'public_catering'"},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'}),
            'time_closed': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(22, 0)'}),
            'time_opening': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'})
        }
    }

    complete_apps = ['public_catering']