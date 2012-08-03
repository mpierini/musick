# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Song'
        db.create_table('players_song', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('players', ['Song'])


    def backwards(self, orm):
        # Deleting model 'Song'
        db.delete_table('players_song')


    models = {
        'players.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['players']