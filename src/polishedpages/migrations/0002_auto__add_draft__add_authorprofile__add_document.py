# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Draft'
        db.create_table(u'polishedpages_draft', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polishedpages.Document'])),
        ))
        db.send_create_signal('polishedpages', ['Draft'])

        # Adding model 'AuthorProfile'
        db.create_table(u'polishedpages_authorprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('polishedpages', ['AuthorProfile'])

        # Adding model 'Document'
        db.create_table(u'polishedpages_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polishedpages.AuthorProfile'])),
        ))
        db.send_create_signal('polishedpages', ['Document'])


    def backwards(self, orm):
        # Deleting model 'Draft'
        db.delete_table(u'polishedpages_draft')

        # Deleting model 'AuthorProfile'
        db.delete_table(u'polishedpages_authorprofile')

        # Deleting model 'Document'
        db.delete_table(u'polishedpages_document')


    models = {
        'polishedpages.authorprofile': {
            'Meta': {'object_name': 'AuthorProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'polishedpages.document': {
            'Meta': {'object_name': 'Document'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polishedpages.AuthorProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'polishedpages.draft': {
            'Meta': {'object_name': 'Draft'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polishedpages.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['polishedpages']