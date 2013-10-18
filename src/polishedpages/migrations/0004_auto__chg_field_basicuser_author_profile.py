# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BasicUser.author_profile'
        db.alter_column(u'polishedpages_basicuser', 'author_profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polishedpages.AuthorProfile'], null=True))

    def backwards(self, orm):

        # Changing field 'BasicUser.author_profile'
        db.alter_column(u'polishedpages_basicuser', 'author_profile_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['polishedpages.AuthorProfile']))

    models = {
        'polishedpages.authorprofile': {
            'Meta': {'object_name': 'AuthorProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'polishedpages.basicuser': {
            'Meta': {'object_name': 'BasicUser'},
            'author_profile': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['polishedpages.AuthorProfile']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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