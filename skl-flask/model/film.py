
class Film():
    def __init__(self):
        self._film_id = None
        self._title = None
        self._description = None
        self._release_year = None
        self._language_id = None
        self._original_language_id = None
        self._rental_duration = None
        self._rental_rate = None
        self._length = None
        self._replacement_cost = None
        self._rating = None
        self._special_features = None
        self._last_update = None
        self._actor_ids = []
        self._category_id = None


    @property
    def film_id(self):
        return self._film_id

    @film_id.setter
    def film_id(self, filmId):
        self._film_id = filmId

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, release_year):
        self._release_year = release_year

    @property
    def language_id(self):
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        self._language_id = language_id

    @property
    def original_language_id(self):
        return self._original_language_id

    @original_language_id.setter
    def original_language_id(self):
        return self._original_language_id

    @property
    def rental_duration(self, ):
        return self._rental_duration

    @rental_duration.setter
    def rental_duration(self, rental_duration):
        self._rental_duration = rental_duration

    @property
    def rental_rate(self):
        return self._rental_rate

    @rental_rate.setter
    def rental_rate(self, rental_rate):
        self._rental_rate = rental_rate

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def replacement_cost(self):
        return self._replacement_cost

    @replacement_cost.setter
    def replacement_cost(self, replacement_cost):
        self._replacement_cost = replacement_cost

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    @property
    def special_features(self):
        return self._special_features

    @special_features.setter
    def special_features(self, special_features):
        self._special_features = special_features

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        self._last_update = last_update

    @property
    def actor_ids(self):
        return self._actor_ids

    @actor_ids.setter
    def actor_ids(self, actor_id):
        self._actor_ids = actor_id

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id



class FilmActor():

    def __init__(self):
        self._actor_id = None
        self._film_id = None
        self._last_update = None

    @property
    def actor_id(self):
        return self._actor_id

    @actor_id.setter
    def actor_id(self, actor_id):
        self._actor_id = actor_id

    @property
    def film_id(self):
        return self._film_id

    @film_id.setter
    def film_id(self, film_id):
        self._film_id = film_id

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        self._last_update = last_update


class FilmCategory():
    def __init__(self):
        self._film_id = None
        self._category_id = None
        self._last_update = None

    @property
    def film_id(self):
        return self._film_id

    @film_id.setter
    def film_id(self, film_id):
        self._film_id = film_id

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        self._last_update = last_update


class FilmText():
  def __init__(self):
    self._film_id = None
    self._title = None
    self._description = None

  @property
  def film_id(self):
    return self._film_id

  @film_id.setter
  def film_id(self, film_id):
    self._film_id = film_id

  @property
  def title(self):
    return self._title

  @title.setter
  def title(self, title):
    self._title = title

  @property
  def description(self):
    return self._description

  @description.setter
  def description(self, description):
    self._description = description