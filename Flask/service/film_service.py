from shared.db_utils import DButils
from datetime import datetime
from shared.utils import objectview



class FilmService():

    filmService = None

    @staticmethod
    def getInstance():
        if FilmService.filmService is None:
            FilmService.filmService = FilmService()

        return FilmService.filmService

    def getFilms(self):
      result = DButils.executemany(FilmSql.SELECT_FILMS)
      return result

    def getFilmsById(self, id):
      result = DButils.execute(FilmSql.SELECT_FILMINFO_BY_ID, (id))
      return result


    def getFilmsByLanguageId(self, languageId):
        result = DButils.executemany(FilmSql.SELECT_FILMINFO_BY_LANGUAGE, (languageId))
        return result


    def getFilmsByActorName(self, name):
        result = DButils.executemany(FilmSql.SELECT_FILMINFO_BY_ACTOR, (name))
        return result


    def getFilmsByCategory(self, category):
        result = DButils.executemany(FilmSql.SELECT_FILMINFO_BY_CATEGORY, (category))
        return result

    def addFilm(self, film):
        try:
          film = objectview(film)
          _sqls = [
            {
              'query': FilmSql.INSERT_FILM,
              'args': (
                film.title or None,
                film.description or None,
                film.release_year or None,
                film.language_id or None,
                film.original_language_id or None,
                film.rental_duration or 0,
                film.rental_rate or 0,
                film.length or None,
                film.replacement_cost or 0,
                film.rating or None,
                film.special_features or None)
            }
          ]

          _sqls.append({
            'query': FilmSql.INSERT_FILM_CATEGORY,
            'args': (film.category_id)
          })

          for actor_id in film.actor_ids:
              _sqls.append({
                'query': FilmSql.INSERT_FILM_ACTOR,
                'args': (actor_id)
              })
          DButils.executeSqls(_sqls)
          return True
        except Exception as e:
          raise Exception(e)

    def updateFilm(self, film):
        try:
          pass
          # get film
          filmDB = DButils.execute(FilmSql.SELECT_FILM_BY_ID, film['film_id'])
          film = objectview({**filmDB, **film})

          # update film film_actor film_category
          _sqls = []
          _sqls.append(
                {
                  'query': FilmSql.UPDATE_FILM,
                  'args': (
                    film.title or None,
                    film.description or None,
                    film.release_year or None,
                    film.language_id or None,
                    film.original_language_id or None,
                    film.rental_duration or 0,
                    film.rental_rate or 0,
                    film.length or None,
                    film.replacement_cost or 0,
                    film.rating or None,
                    film.special_features or None,
                    film.film_id)
                }
              )

          if film.category_id is not None:
              _sqls.append({
                'query': FilmSql.UPDATE_CATEGORY_FILM,
                'args': (
                  film.category_id,
                  film.film_id
                  )
              })

          if film.actor_ids is not None and len(film.actor_ids) > 0:

              _sqls.append({
                'query': FilmSql.DELETE_ACTOR_FILM,
                'args': film.film_id
              })

              for actor_id in film.actor_ids:
                  _sqls.append({
                    'query': FilmSql.INSERT_ACTOR_FILM_WITH_ID,
                    'args': (
                      actor_id,
                      film.film_id
                    )
                  })

          return DButils.executeSqls(_sqls)
        except Exception as e:
          raise e


    def deleteFilm(self, id):
        try:
          sqls = [
            {
              'query': FilmSql.DELETE_ACTOR_FILM,
              'args': id
            },
            {
              'query': FilmSql.DELETE_CATEGORY_FILM,
              'args': id
            },
            {
              'query': FilmSql.DELETE_FILM,
              'args': id
            }
          ]

          return DButils.executeSqls(sqls)
        except Exception as e:
          raise e




class FilmSql():
    SELECT_FILMS = 'select * from film_list'
    SELECT_FILMINFO_BY_ID = 'select * from film_list where FID=%s'
    SELECT_FILM_BY_ID = 'select * from film where film_id = %s'
    SELECT_FILMINFO_BY_LANGUAGE = 'select * from film_list where FID in (select film_id from film where language_id=%s)'
    SELECT_FILMINFO_BY_ACTOR = 'select * from film_list where INSTR(actors, %s) > 0'
    SELECT_FILMINFO_BY_CATEGORY = 'select * from film_list where INSTR(category, %s) > 0'
    INSERT_FILM = 'insert into film(title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    INSERT_FILM_ACTOR = 'insert into film_actor(film_id, actor_id) values (LAST_INSERT_ID(), %s)'
    INSERT_FILM_CATEGORY = 'insert into film_category(film_id, category_id) values (LAST_INSERT_ID(), %s)'
    INSERT_CATEGORY_FILM_WITH_ID = 'insert into film_category(film_id, category_id) values(%s, %s)'
    INSERT_ACTOR_FILM_WITH_ID = 'insert into film_actor(actor_id, film_id) values(%s, %s)'
    UPDATE_FILM = 'update film set title = %s, description = %s, release_year = %s, language_id = %s, original_language_id = %s, rental_duration = %s, rental_rate = %s, length = %s, replacement_cost = %s, rating = %s, special_features = %s where film_id = %s'
    UPDATE_CATEGORY_FILM = 'update film_category set category_id = %s where film_id = %s'
    DELETE_ACTOR_FILM = 'delete from film_actor where film_id = %s'
    DELETE_FILM = 'delete from film where film_id = %s'
    DELETE_CATEGORY_FILM = 'delete from film_category where film_id = %s'
