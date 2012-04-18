# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PublicCatering.phone'
        db.add_column('public_catering', 'phone',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'PublicCatering.address'
        db.add_column('public_catering', 'address',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'PublicCatering.site'
        db.add_column('public_catering', 'site',
                      self.gf('django.db.models.fields.URLField')(default=u'', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'PublicCatering.description'
        db.add_column('public_catering', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1000, blank=True),
                      keep_default=False)

        # Adding field 'PublicCatering.time_opening'
        db.add_column('public_catering', 'time_opening',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(10, 0)),
                      keep_default=False)

        # Adding field 'PublicCatering.time_closed'
        db.add_column('public_catering', 'time_closed',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(22, 0)),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'PublicCatering.phone'
        db.delete_column('public_catering', 'phone')

        # Deleting field 'PublicCatering.address'
        db.delete_column('public_catering', 'address')

        # Deleting field 'PublicCatering.site'
        db.delete_column('public_catering', 'site')

        # Deleting field 'PublicCatering.description'
        db.delete_column('public_catering', 'description')

        # Deleting field 'PublicCatering.time_opening'
        db.delete_column('public_catering', 'time_opening')

        # Deleting field 'PublicCatering.time_closed'
        db.delete_column('public_catering', 'time_closed')

    models = {
        'public_catering.publiccatering': {
            'Meta': {'object_name': 'PublicCatering', 'db_table': "'public_catering'"},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '20', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'default': "u''", 'max_length': '200', 'blank': 'True'}),
            'time_closed': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(22, 0)'}),
            'time_opening': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(10, 0)'})
        }
    }

    complete_apps = ['public_catering']