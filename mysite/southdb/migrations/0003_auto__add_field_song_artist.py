# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Song.artist'
        db.add_column('southdb_song', 'artist',
                      self.gf('django.db.models.fields.CharField')(default='Artist Name', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Song.artist'
        db.delete_column('southdb_song', 'artist')


    models = {
        'southdb.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['southdb']