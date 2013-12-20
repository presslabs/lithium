import datetime

from sqlalchemy.orm.collections import InstrumentedList

from lithium.declarative import BaseSQLAlchemy as SQLAlchemy
db = SQLAlchemy()

class AlchemyDecoder(dict):

  def __init__(self, model, ignore=None, eager_list=None):
    model_dict = self.__model_to_dict__(model, ignore, eager_list)

    super(AlchemyDecoder, self).__init__(**model_dict)

  def __model_to_dict__(self, model, ignore, eager_list=None):
    if not eager_list:
      eager_list = []

    if not ignore:
      ignore = []

    result = {}

    for key in model.__mapper__.c.keys() + eager_list:
      # TODO: Implement ignore key
      if not key.startswith('_'):
        field = getattr(model, key)

        if (isinstance(field, InstrumentedList) or isinstance(field, list)) and key in eager_list:
          partial_result = []
          for item in field:
            partial_result.append(
              self.__model_to_dict__(item, ignore, item.__eager__)
            )

          field = partial_result

        if isinstance(field, db.Model) and key in eager_list:
          field = self.__model_to_dict__(field, ignore, field.__eager__)
        elif isinstance(field, datetime.date):
          field = datetime_obj_to_string(field)

        result[key] = field

    return result
