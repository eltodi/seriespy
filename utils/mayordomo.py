# http://dpaste.com/803186/

import urllib2
import bs4
import transmissionrpc
import re
import imdb
from series.models import *
from utils.slugify import slugify

EZTV_SHOW_PAGE = "http://eztv.it/shows/%d/"
MY_SHOWS = (36,255)
HD = True
TRANSMISSION_HOST = "127.0.0.1"
TRANSMISSION_USER = "jack"
TRANSMISSION_PASS = "sparrow"
RX_IMDB_URL_ID = re.compile("http://www.imdb.com/title/tt(\d+)/")

def get_all_shows():
    dom = get_url("http://eztv.it/showlist/")
    rows = dom.findAll("a", {"class":"thread_link"})
    api = imdb.IMDb()
    shows = []
    for row in rows:
        title = row.text
        eztv_id = row.attrs["href"].split("/")[2]
        status = row.find_parent().find_parent().findAll("td")[1].find("font").text

        try:
            print title,
            serie = api.search_movie(title=title)[0]
            print " [OK]"
            if serie.get("title") == title:
                shows.append({
                    "title":title,
                    "status":status,
                    "eztv_id":eztv_id,
                    "imdb":serie
                    })
        except:
            print "[Not Found]"
    return shows


def cargar_datos(shows):
    import imdb
    from series.models import Serie, Genero
    from utils.slugify import slugify

    api = imdb.IMDb()
    for show in shows:
        try:
            try:
                datos = api.get_movie( show["imdb"].movieID )
            except:
                continue
            s = Serie()
            s.titulo = datos.get("title")
            print s.titulo
            s.slug = slugify(s.titulo)
            try:
                s.productora = (",".join( [c.get("name") for c in datos.get("production companies")] ))[:255]
            except:
                pass
            s.director = datos.get("director")
            s.estado = show["status"]
            try:
                s.plot = datos.get("plot")[0]
            except:
                pass
            s.mini_plot = datos.get("plot outline")
            s.year = datos.get("year")
            s.cover = datos.get("full-size cover url")
            s.min_cover = datos.get("cover url")
            s.rating = datos.get("rating")
            if not s.rating:
                s.rating = 0
            s.imdb_id = show["imdb"].movieID
            s.save()
            for g in datos.get("genres"):
                gen, created = Genero.objects.get_or_create(nombre=g)
                s.genero.add( gen )
        except:
            pass

def cargar_episodios(shows):
    for show in shows:
        links = get_all_episodes(show["eztv_id"])
        episodes = api.get_movie_episodes(show["imdb"].movieID)
        serie = Serie.objects.get(titulo=show["title"])
        for link in links:
            season, epinumber = get_episode_season(link)
            title = episodes["data"]["episodes"][season][epinumber].get("title")
            ep = Episodio(serie=serie)
            ep.titulo = title
            ep.titulo_raw = link.text
            ep.temporada = season
            ep.numero = epinumber
            ep.url_magnet = get_episode_link(link)
            ep.save()

def get_url(url):
    f = urllib2.urlopen(url)
    html = f.read()
    f.close()
    dom = bs4.BeautifulSoup(html)
    return dom

def get_all_episodes(show_id):
    dom = get_url(EZTV_SHOW_PAGE % show_id)
    episodes_links = dom.findAll("a", {"class":"epinfo"})

    return episodes_links

def get_episode_season(episode_link):
    rx = re.compile("S(\d+)E(\d+)")
    try:
        return tuple( [int(elem) for elem in rx.findall(episode_link.text)[0] ] )
    except:
        rx = re.compile("(\d+)x(\d+)")
        try:
            return tuple( [int(elem) for elem in rx.findall(episode_link.text)[0] ] )
        except:
            return None

def get_latest_episode(show_id):
    dom = get_url(EZTV_SHOW_PAGE % show_id)
    episodes_links = dom.findAll("a", {"class":"epinfo"})

    i = 0
    latest = episodes_links[0]
    if HD:
        while "720p" not in latest.text and i<len(episodes_links):
            i += 1
            latest = episodes_links[i]

    return latest

def get_episode_age(episode_link):
    age = episode_link.find_parent().find_parent().findAll("td")[3]
    return age.text

def valid_age(age):
    if "d" in age:
        if "1d" in age:
            return True
        return False
    else:
        if "week" in age:
            return False
    return True

def get_episode_link(epi):
    return epi.find_parent().find_parent().find_all("td")[2].find_all("a",{"title":"Magnet Link"})[0].attrs["href"]


def novedades():
    links = []
    for show_id in MY_SHOWS:
        epi = get_latest_episode(show_id)
        if valid_age( get_episode_age(epi) ):
            links.append( get_episode_link(epi) )

    client = transmissionrpc.Client(address=TRANSMISSION_HOST, user=TRANSMISSION_USER, password=TRANSMISSION_PASS)
    for link in links:
        client.add_uri(link)

    print "%d link(s) nuevo(s) descargandose..." % len(links)


def get_show_info(show_id):
    dom = get_url(EZTV_SHOW_PAGE % show_id)
    table = dom.find("table", {"class":"section_thread_post show_info_description"})
    info = table.findAll("td")[0].text
    return info

def get_show_imdb_id(show_info):
    return RX_IMDB_URL_ID.findall(show_info)[0]

def get_show_imdb_info(imdb_id):
    from imdb import IMDb
    ia = IMDb()
    return ia.get_movie(imdb_id)

def get_cover_thumb(movie):
    return movie.get("cover url")

def get_cover_full(movie):
    return movie.get("full-size cover url")