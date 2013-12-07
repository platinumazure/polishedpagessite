# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AuthorProfile.public_name'
        db.add_column(u'polishedpages_authorprofile', 'public_name',
                      self.gf('django.db.models.fields.CharField')(default='Update Me', max_length=100, db_index=True),
                      keep_default=False)

        # Adding field 'AuthorProfile.about'
        db.add_column(u'polishedpages_authorprofile', 'about',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140, blank=True),
                      keep_default=False)

        # Adding field 'AuthorProfile.verbose_about'
        db.add_column(u'polishedpages_authorprofile', 'verbose_about',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding M2M table for field favorite_authors on 'AuthorProfile'
        db.create_table(u'polishedpages_authorprofile_favorite_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_authorprofile', models.ForeignKey(orm['polishedpages.authorprofile'], null=False)),
            ('to_authorprofile', models.ForeignKey(orm['polishedpages.authorprofile'], null=False))
        ))
        db.create_unique(u'polishedpages_authorprofile_favorite_authors', ['from_authorprofile_id', 'to_authorprofile_id'])


    def backwards(self, orm):
        # Deleting field 'AuthorProfile.public_name'
        db.delete_column(u'polishedpages_authorprofile', 'public_name')

        # Deleting field 'AuthorProfile.about'
        db.delete_column(u'polishedpages_authorprofile', 'about')

        # Deleting field 'AuthorProfile.verbose_about'
        db.delete_column(u'polishedpages_authorprofile', 'verbose_about')

        # Removing M2M table for field favorite_authors on 'AuthorProfile'
        db.delete_table('polishedpages_authorprofile_favorite_authors')


    models = {
        'polishedpages.authorprofile': {
            'Meta': {'object_name': 'AuthorProfile'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'favorite_authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorite_authors+'", 'symmetrical': 'False', 'to': "orm['polishedpages.AuthorProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polishedpages.BasicUser']"}),
            'verbose_about': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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