from flask import Blueprint, request
from service.film_service import FilmService
import json

film_route = Blueprint('film_app', __name__)
filmService = FilmService.getInstance()

@film_route.route('/films')
def getFilms():
    result = filmService.getFilms()
    return json.dumps(result, default=str)

@film_route.route('/films/<string:id>')
def getFilmById(id):
    result = filmService.getFilmsById(id)
    return json.dumps(result, default=str)

@film_route.route('/actors/<string:name>/films')
def getFilmsByActor(name):
    result = filmService.getFilmsByActorName(name)
    return json.dumps(result, default=str)

@film_route.route('/categorys/<string:category>/films')
def getFilmsByCategory(category):
    result = filmService.getFilmsByCategory(category)
    return json.dumps(result, default=str)

@film_route.route('/languages/<string:language>/films')
def getFilmsByLanguage(language):
    result = filmService.getFilmsByLanguageId(language)
    return json.dumps(result, default=str)

@film_route.route('/films',  methods=['POST'])
def addFilm():
    film = request.json
    result = filmService.addFilm(film)
    return json.dumps(result, default=str)

@film_route.route('/films/<string:id>', methods=['POST', 'PATCH'])
def updateFilm(id):
    film = request.json
    result = filmService.updateFilm(film)
    return json.dumps(result, default=str)

@film_route.route('/films/<string:id>', methods=['DELETE'])
def deleteFilm(id):
    result = filmService.deleteFilm(id)
    return json.dumps(result, default=str)
