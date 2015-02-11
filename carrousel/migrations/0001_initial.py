# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrousel'
        db.create_table(u'carrousel_carrousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('interval', self.gf('django.db.models.fields.IntegerField')()),
            ('show_indicators', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'carrousel', ['Carrousel'])

        # Adding model 'Slide'
        db.create_table(u'carrousel_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carrousel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['carrousel.Carrousel'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('mobile_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('html_position', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'carrousel', ['Slide'])


    def backwards(self, orm):
        # Deleting model 'Carrousel'
        db.delete_table(u'carrousel_carrousel')

        # Deleting model 'Slide'
        db.delete_table(u'carrousel_slide')


    models = {
        u'carrousel.carrousel': {
            'Meta': {'object_name': 'Carrousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'show_indicators': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'carrousel.slide': {
            'Meta': {'ordering': "['position']", 'object_name': 'Slide'},
            'carrousel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['carrousel.Carrousel']"}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html_position': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mobile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['carrousel']