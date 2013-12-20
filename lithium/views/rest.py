import json

from lithium.decoder import AlchemyDecoder
from lithium.views.base import BaseView
from lithium.exceptions import HttpNotFound, HttpBadRequest

from flask.ext.classy import FlaskView
from lithium.views import BaseView
from flask import request

class RESTView(BaseView):

  def get(self, entity_id):
    if(hasattr(self, "show")):
      return self.show(entity_id)
    else:
      raise NotImplemented("No method found with the name show")

  def post(self):
    if(hasattr(self, "create")):
      return self.create()
    else:
      raise NotImplemented("No method found with the name create")

  def put(self, entity_id):
    if(hasattr(self, "update")):
      return self.update(entity_id)
    else:
      raise NotImplemented("No method found with the name update")

  def patch(self):
    if(hasattr(self, "update")):
      return self.update(entity_id)
    else:
      raise NotImplemented("No method found with the name update")

class RESTModelView(RESTView):
  model = None
  __exclude__ = []
  db = None

  def create(self):
    data = json.loads(request.data)
    item = self.model(**data)

    if not item.valid:
      raise HttpBadRequest(item.errors)

    self.db.session.add(item)
    self.db.session.commit()

    return AlchemyDecoder(item, self.__exclude__)

  def index(self):
    items = self.model.query.all()
    items = [AlchemyDecoder(item, self.__exclude__) for item in items]
    return items

  def show(self, entity_id):
    item = self.model.query.get(entity_id)

    if item:
      return AlchemyDecoder(item, self.__exclude__)
    else:
      raise HttpNotFound({'error': 'Item not found in database'})

  def update(self, entity_id):
    data = json.loads(request.data)
    item = self.model.query.get(entity_id)

    if not item:
      raise HttpNotFound({'error': 'Item not found in database'})

    for field in data:
      if hasattr(item, field):
        setattr(item, field, data[field])

    if not item.valid:
      raise HttpBadRequest(item.errors)

    self.db.session.add(item)
    self.db.session.commit()

    return AlchemyDecoder(item, self.__exclude__)

  def delete(self, entity_id):
    item = self.model.query.get(entity_id)

    if item:
      self.db.session.delete(item)
      self.db.session.commit()
      return {'success': 'Item was deleted!'}
    else:
      raise HttpNotFound({'error': 'Item not found in database'})
