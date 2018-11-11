import json
from flask import Blueprint, json, request

from service.actor_service import ActorService
from shared.utils import objectview


actor_route = Blueprint('actor_route', __name__)
actorService = ActorService.getInstance()

@actor_route.route('/actors')
def getActors():
    result = actorService.getActor()
    return json.dumps(result, default=str, indent=4, separators=(',', ': '))

@actor_route.route('/actors/<string:id>')
def getActorById(id):
    result = actorService.getActorById(id)
    print(json.dumps(result, default=str))
    return json.dumps(result, default=str)

@actor_route.route('/films/<string:film_id>/actors')
def getActorsByFilmId(film_id):
    result = actorService.getActorsByFilmId(film_id)
    print(json.dumps(result, default=str))
    return json.dumps(result, default=str)

@actor_route.route('/actors/', methods=['POST'])
def addActor():
    actor = request.json
    result = actorService.addActor(actor)
    return result

@actor_route.route('/actors/<string:id>', methods=['PATCH'])
def updateActor(id):
    actor = request.json
    result = actorService.updateActor(id, actor)
    return json.dumps(result, default=str)

@actor_route.route('/actors/<string:id>', methods=['DELETE'])
def deleteActorById(id):
    result = actorService.deleteActorById(id)
    return json.dumps(result, default=str)
