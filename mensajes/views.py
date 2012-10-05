from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from mensajes.forms import MensajeForm
from mensajes.models import Mensaje
from series.models import Serie
from utils.decorators import render_with, ajax_request


@login_required
@csrf_exempt
@ajax_request
def hay_mensajes_pendientes_ajax(request):
    mensajes_pendientes = Mensaje.objects.filter(destinatario=request.user, visto=False).order_by('fecha')

    mensajes = []
    for mensaje in mensajes_pendientes:
        mensajes.append((
            mensaje.remitente.username,
            mensaje.texto,
            mensaje.fecha.isoformat()
        ))
    mensajes_pendientes.update(visto=True)

    return mensajes


@login_required
@render_with('mensajes/enviar_mensaje.html')
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.visto = False
            mensaje.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        oSerie = Serie.objects.all().order_by('-rating')[:1]
        form = MensajeForm()

    return {'form': form, 'oSeries':oSerie}

@csrf_exempt
def pruebame(request):
    return HttpResponse(request.POST["op"])











