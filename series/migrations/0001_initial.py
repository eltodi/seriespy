# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PerfilUsuario'
        db.create_table('series_perfilusuario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('transmission_host', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('transmission_port', self.gf('django.db.models.fields.IntegerField')(default=9091)),
            ('transmission_user', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('transmission_password', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('series', ['PerfilUsuario'])

        # Adding model 'Genero'
        db.create_table('series_genero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('series', ['Genero'])

        # Adding model 'Serie'
        db.create_table('series_serie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('productora', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('imdb_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cover', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('min_cover', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('plot', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mini_plot', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=1)),
        ))
        db.send_create_signal('series', ['Serie'])

        # Adding M2M table for field genero on 'Serie'
        db.create_table('series_serie_genero', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serie', models.ForeignKey(orm['series.serie'], null=False)),
            ('genero', models.ForeignKey(orm['series.genero'], null=False))
        ))
        db.create_unique('series_serie_genero', ['serie_id', 'genero_id'])

        # Adding model 'Episodio'
        db.create_table('series_episodio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['series.Serie'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('titulo_raw', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('temporada', self.gf('django.db.models.fields.IntegerField')()),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('url_magnet', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('series', ['Episodio'])

        # Adding model 'EpisodioUsuario'
        db.create_table('series_episodiousuario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('episodio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['series.Episodio'])),
            ('rating', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=1)),
            ('fecha_visto', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('fecha_descarga', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('series', ['EpisodioUsuario'])

        # Adding model 'UsuarioSerie'
        db.create_table('series_usuarioserie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['series.Serie'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desde', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('series', ['UsuarioSerie'])

        # Adding model 'RegistroImportacion'
        db.create_table('series_registroimportacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cuando', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('series', ['RegistroImportacion'])


    def backwards(self, orm):
        # Deleting model 'PerfilUsuario'
        db.delete_table('series_perfilusuario')

        # Deleting model 'Genero'
        db.delete_table('series_genero')

        # Deleting model 'Serie'
        db.delete_table('series_serie')

        # Removing M2M table for field genero on 'Serie'
        db.delete_table('series_serie_genero')

        # Deleting model 'Episodio'
        db.delete_table('series_episodio')

        # Deleting model 'EpisodioUsuario'
        db.delete_table('series_episodiousuario')

        # Deleting model 'UsuarioSerie'
        db.delete_table('series_usuarioserie')

        # Deleting model 'RegistroImportacion'
        db.delete_table('series_registroimportacion')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'series.episodio': {
            'Meta': {'object_name': 'Episodio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['series.Serie']"}),
            'temporada': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'titulo_raw': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_magnet': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'series.episodiousuario': {
            'Meta': {'object_name': 'EpisodioUsuario'},
            'episodio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['series.Episodio']"}),
            'fecha_descarga': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_visto': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'series.genero': {
            'Meta': {'object_name': 'Genero'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'series.perfilusuario': {
            'Meta': {'object_name': 'PerfilUsuario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transmission_host': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'transmission_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'transmission_port': ('django.db.models.fields.IntegerField', [], {'default': '9091'}),
            'transmission_user': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'series.registroimportacion': {
            'Meta': {'object_name': 'RegistroImportacion'},
            'cuando': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'series.serie': {
            'Meta': {'object_name': 'Serie'},
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['series.Genero']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'min_cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mini_plot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plot': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'productora': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'series.usuarioserie': {
            'Meta': {'object_name': 'UsuarioSerie'},
            'desde': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['series.Serie']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['series']