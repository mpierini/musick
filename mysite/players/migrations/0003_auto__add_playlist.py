# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Playlist'
        db.create_table('players_playlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('players', ['Playlist'])

        # Adding M2M table for field songs on 'Playlist'
        db.create_table('players_playlist_songs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playlist', models.ForeignKey(orm['players.playlist'], null=False)),
            ('song', models.ForeignKey(orm['players.song'], null=False))
        ))
        db.create_unique('players_playlist_songs', ['playlist_id', 'song_id'])


    def backwards(self, orm):
        # Deleting model 'Playlist'
        db.delete_table('players_playlist')

        # Removing M2M table for field songs on 'Playlist'
        db.delete_table('players_playlist_songs')


    models = {
        'players.playlist': {
            'Meta': {'object_name': 'Playlist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': "orm['players.Song']"})
        },
        'players.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['players']