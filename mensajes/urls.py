from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^enviar/$','mensajes.views.enviar_mensaje', name='mensajes_enviar_mensaje'),
	url(r'^pendientes/$' , 'mensajes.views.hay_mensajes_pendientes_ajax', name='mensajes_hay_mensajes_pendientes_ajax'),
	url(r'^pruebame/$', 'mensajes.views.pruebame', name='mensajes_pruebame'),
)