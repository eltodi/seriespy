# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import Context, RequestContext
from series.models import *
from series.forms import *
from utils import slugify

def pruebas(request):
	oSeries = Serie.objects.all().order_by("-rating")[:50]

	c = Context({
		"oSeries" : oSeries,
	})
	return render_to_response("series/pruebas.html", c)

def home(request):
	oSeries = Serie.objects.all().order_by("?")[:40]
	c = Context({
		"oSeries" : oSeries,
	})
	return render_to_response("series/home.html", c)

def ver_ficha_serie(request, slug_serie):
	serie = get_object_or_404(Serie, slug=slug_serie)
	temporadas = serie.episodio_set.values_list("temporada", flat=True).order_by("temporada").distinct()


	c = Context({
		"obj" : serie,
		"oTemporadas" : temporadas,
	})

	return render_to_response("series/ver_ficha_serie.html", c)

def ver_listado_episodios(request, slug_serie, temporada):
	serie = get_object_or_404(Serie, slug=slug_serie)
	episodios = serie.episodio_set.filter(temporada = temporada)

	c = Context({
		"oSerie" : serie,
		"temporada" : temporada,
		"oEpisodios" : episodios,
	})
	return render_to_response("series/ver_listado_episodios.html", c)


def ver_ficha_episodio(request, slug_serie, temporada, num_episodio):
	serie = get_object_or_404(Serie, slug=slug_serie)
	episodio = serie.episodio_set.filter(temporada = temporada, numero = num_episodio)[0]

	c = Context({
		"oSerie" : serie,
		"oEpisodio" : episodio,
	})

	return render_to_response("series/ver_ficha_episodio.html", c)

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

			return HttpResponseRedirect(reverse("series_home"))		# reverse es para ir al name del url.py
		'''
		# UTILIZANDO formulario generado desde el modelo
		form = SerieForm2(request.POST)
		if form.is_valid():
			nueva_serie = form.save(commit = False)
			nueva_serie.slug = slugify.slugify(nueva_serie.titulo)
			nueva_serie.save()

			return HttpResponseRedirect(reverse("series_home"))

	else:
		form = SerieForm2()

	return render_to_response("series/serie_nueva.html", {"form": form,}, context_instance=RequestContext(request))


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







