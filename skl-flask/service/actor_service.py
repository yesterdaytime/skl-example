from shared.db_utils import DButils
from shared.utils import objectview


class ActorService():

    actorService = None

    @staticmethod
    def getInstance():
        if ActorService.actorService is None:
            ActorService.actorService = ActorService()
        return ActorService.actorService

    def getActor(self):
        result = DButils.executemany(ActorSql.select_actor, None)
        return result


    def getActorById(self, id):
        result = DButils.execute(ActorSql.select_actor_by_id, (id))
        return result


    def getActorsByFilmId(self, id):
        result = DButils.executemany(ActorSql.select_actor_by_film_id, (id))
        return result

    def addActor(self, actor):
        try:
            actor = objectview(actor)
            DButils.execute(ActorSql.insert_actor, (actor.first_name, actor.last_name), True)
            return 'OK'
        except Exception as e:
            raise e


    def updateActor(self, id, actor):
        actorTemp = self.getActorById(id)
        actorTemp = objectview({**actorTemp, **actor})
        DButils.executemany(ActorSql.update_actor, (actorTemp.first_name, actorTemp.last_name, id), True)
        return self.getActorById(id)


    def deleteActorById(self, id):
        try:
            DButils.executemany(ActorSql.delete_actor, id)
            return 'OK'
        except Exception as e:
            raise e


class ActorSql():
    select_actor = 'select * from actor'
    select_actor_by_id = 'select * from actor where actor_id = %s'
    select_actor_by_film_id = 'select * from actor where actor_id in (select actor_id from film_actor where film_id = %s)'
    insert_actor = 'insert into actor(first_name, last_name) values(%s, %s)'
    update_actor = 'update actor set first_name=%s,last_name=%s where actor_id=%s'
    delete_actor = 'delete from actor where actor_id=%s'

