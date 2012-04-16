# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PublicCatering'
        db.create_table('public_catering', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=100)),
        ))
        db.send_create_signal('public_catering', ['PublicCatering'])

    def backwards(self, orm):
        # Deleting model 'PublicCatering'
        db.delete_table('public_catering')

    models = {
        'public_catering.publiccatering': {
            'Meta': {'object_name': 'PublicCatering', 'db_table': "'public_catering'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100'})
        }
    }

    complete_apps = ['public_catering']