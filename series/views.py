# Create your views here.
import datetime
from django.db.models import Count
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import Context, RequestContext
from series.models import *
from series.forms import *
from utils import slugify
from utils.decorators import render_with, ajax_request
import requests
from django.views.decorators.csrf import csrf_exempt
import pytz
import twitter


def pruebas(request):
	oSeries = Serie.objects.all().order_by("-rating")[:50]

	c = Context({
		"oSeries" : oSeries,
	})
	return render_to_response("series/pruebas.html", c)


@render_with("series/home.html")
def home(request):
	oAleatorias = Serie.objects.filter(min_cover__icontains="http://").order_by("?")[:24]
	oSeries = Serie.objects.filter(min_cover__icontains="http://").order_by("-rating")[:30]
	api = twitter.Api();
	oTwitter = api.GetUserTimeline("@django_es")[:5]

	return {"oSeries":oSeries, "oAleatorias":oAleatorias, "oTwitter":oTwitter}


@render_with("series/home.html")
def search(request):
	if request.method=="GET":
		oSeries = Serie.objects.filter(titulo__icontains=request.GET["titulo"])
		if oSeries.count()<1:
			#raise Http404
			return HttpResponseRedirect(reverse("series_home"))
		return {"oSeries":oSeries}
	else:
		return HttpResponseRedirect(reverse("series_home"))


@render_with("series/ver_ficha_serie.html")
def ver_ficha_serie(request, slug_serie):
	serie = get_object_or_404(Serie, slug=slug_serie)
	temporadas = serie.episodio_set.values_list("temporada", flat=True).order_by("temporada").distinct()

	return {"obj": serie, "oTemporadas": temporadas}


@render_with("series/ver_listado_episodios.html")
def ver_listado_episodios(request, slug_serie, temporada):
	serie = get_object_or_404(Serie, slug=slug_serie)
	episodios = serie.episodio_set.filter(temporada = temporada)

	c = Context({
		"oSerie" : serie,
		"temporada" : temporada,
		"oEpisodios" : episodios,
	})
	return c


@render_with("series/ver_ficha_episodio.html")
def ver_ficha_episodio(request, slug_serie, temporada, num_episodio):
	serie = get_object_or_404(Serie, slug=slug_serie)
	episodio = serie.episodio_set.filter(temporada = temporada, numero = num_episodio)[0]

	c = Context({
		"oSerie" : serie,
		"oEpisodio" : episodio,
	})
	return c


@login_required
def serie_nueva(request):
	if request.method == "POST":
		# UTILIZANDO formulario creado a mano
		'''
		form = SerieForm(request.POST)
		if form.is_valid():
			serie = Serie()
			serie.titulo = form.cleaned_data["titulo"]
			serie.slug = slugify.slugify(form.cleaned_data["titulo"])
			serie.rating =  5.0
			serie.save()

			return HttpResponseRedirect(reverse("series_home"))	# reverse es para ir al name del url.py
		'''
		# UTILIZANDO formulario generado desde el modelo
		form = SerieForm3(request.POST)
		if form.is_valid():
			nueva_serie = form.save(commit = False)
			nueva_serie.slug = slugify.slugify(nueva_serie.titulo)
			nueva_serie.save()

			return HttpResponseRedirect(reverse("series_home"))

	else:
		form = SerieForm3()

	return render_to_response("series/serie_nueva.html", {"form": form,}, context_instance=RequestContext(request))


def portada(request, slug_serie):
	serie = Serie.objects.get(slug = slug_serie)
	r = requests.get(serie.min_cover)
	return HttpResponse(r.content, content_type = "image/jpg")


def episodio_nuevo(request, slug_serie):	#ATENCION:::: RECIBE DOS VARIABLES, UNA DE LA URL.PY
	if request.method == "POST":
		form = EpisodioForm(request.POST)
		if form.is_valid():
			nuevo_episodio = form.save(commit = False)
			serie = get_object_or_404(Serie, slug=slug_serie)

			nuevo_episodio.serie = serie
			nuevo_episodio.save()

			#form.save()
			return HttpResponseRedirect(reverse("series_home"))

	else:
		form = EpisodioForm()

	return render_to_response("series/episodio_nuevo.html", {"form": form}, context_instance=RequestContext(request))


@login_required
@csrf_exempt
@ajax_request
def episodios_descargados_ajax(request):
    episodios_u = EpisodioUsuario.objects.filter(user=request.user)
    now = datetime.datetime.now(tz=pytz.UTC)

    result = []
    for eu in episodios_u:
        if eu.fecha_descarga is not None and abs((now - eu.fecha_descarga).total_seconds()) < 10:
            result.append(
                (eu.episodio.serie.titulo,
                 eu.episodio.numeracion_normalizada(),
                 eu.episodio.titulo))
    return result


@login_required
def notificaciones_cambiar(request, value=False):
	try:
		perfil = request.user.get_profile()
	except PerfilUsuario.DoesNotExist:
		perfil = PerfilUsuario()
		perfil.user = request.user
		perfil.save()
	perfil.notificaciones_activas = value
	perfil.save()

	#raise Http404
	return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("series_home")))


