# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BasicUser.author_profile'
        db.delete_column(u'polishedpages_basicuser', 'author_profile_id')

        # Adding field 'AuthorProfile.user'
        db.add_column(u'polishedpages_authorprofile', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['polishedpages.BasicUser']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BasicUser.author_profile'
        db.add_column(u'polishedpages_basicuser', 'author_profile',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['polishedpages.AuthorProfile'], null=True),
                      keep_default=False)

        # Deleting field 'AuthorProfile.user'
        db.delete_column(u'polishedpages_authorprofile', 'user_id')


    models = {
        'polishedpages.authorprofile': {
            'Meta': {'object_name': 'AuthorProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polishedpages.BasicUser']"})
        },
        'polishedpages.basicuser': {
            'Meta': {'object_name': 'BasicUser'},
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