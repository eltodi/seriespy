from django.contrib import admin
from series.models import PerfilUsuario, Genero, Serie, Episodio, EpisodioUsuario, UsuarioSerie, RegistroImportacion
from mensajes.models import Mensaje

class SerieAdmin(admin.ModelAdmin):
    list_filter = ('genero', 'year')
    ordering = ('titulo',)


class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'serie', 'numeracion_normalizada',)
    list_filter = ('serie__genero', 'temporada',)


admin.site.register(PerfilUsuario)
admin.site.register(Genero)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(EpisodioUsuario)
admin.site.register(UsuarioSerie)
admin.site.register(RegistroImportacion)

admin.site.register(Mensaje)