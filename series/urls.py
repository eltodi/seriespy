from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

'''
    /series/ --> series del dia
    /series/breaking-bad/ ---> ficha de la series
    /series/breaking-bad/1/ ---> listado episodios de la temporada
    /series/breaking-bad/1/1/ ---> ficha del episodio
'''

urlpatterns = patterns('',
	url(r'^$', 'series.views.home', name='series_home'),
    url(r'^pruebas/$', 'series.views.pruebas'),
    url(r'^servicios/$', 'series.views.servicios', name="series_servicios"),
    url(r'^nueva/','series.views.serie_nueva', name='series_serie_nueva'),

    url(r'^notificaciones/descargas/$', 'series.views.episodios_descargados_ajax', name='series_episodios_descargados_ajax'),

    url(r'^notificaciones/activar/$','series.views.notificaciones_cambiar', {'value':True}, name='series_notificaciones_activar'),
    url(r'^notificaciones/desactivar/$','series.views.notificaciones_cambiar', {'value':False}, name='series_notificaciones_desactivar'),


    #url(r'^nuevo/episodio/', 'series.views.episodio_nuevo', name='series_episodio_nuevo'),
    url(r'^(?P<slug_serie>[^/]+)/portada/$', 'series.views.portada', name='series_portada'),
    url(r'^search/$', 'series.views.search', name='series_search'),
    url(r'^(?P<slug_serie>[^/]+)/nuevo/$', 'series.views.episodio_nuevo', name='series_episodio_nuevo'),
    url(r'^(?P<slug_serie>[^/]+)/$', 'series.views.ver_ficha_serie', name='series_ver_ficha_serie'),
    url(r'^(?P<slug_serie>[^/]+)/(?P<temporada>\d+)/$', 'series.views.ver_listado_episodios', name='series_ver_listado_episodios'),
    url(r'^(?P<slug_serie>[^/]+)/(?P<temporada>\d+)/(?P<num_episodio>\d+)/$', 'series.views.ver_ficha_episodio', name='series_ver_ficha_episodio'),
    # Examples:
    # url(r'^$', 'seriespy.views.home', name='home'),
    # url(r'^seriespy/', include('seriespy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
