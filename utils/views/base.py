from functools import wraps
import json

from flask import request

from flask.ext.classy import FlaskView

def get_request_type():
  types = {
    'application/json': 'json',
    'application/xml': 'xml'
  }

  if 'Content-Type' in request.headers:
    if request.headers['Content-Type'] in types:
      return types[request.headers['Content-Type']]

  return 'html'

def serialize_response(request_type, response):
  serializers = {
    'json': lambda response: json.dumps(response),
    'xml': lambda response: json.dumps(response),
  }

  if request_type in serializers:
    return serializers[request_type](response)

  return json.dumps(response) if not isinstance(response, str) else response

def serialize(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    response = f(*args, **kwargs)
    request_type = get_request_type()
    return serialize_response(request_type, response)

  return decorator

class class_property(property):
  def __get__(self, instance, type):
    if instance is None:
        return super(class_property, self).__get__(type, type)
    return super(class_property, self).__get__(instance, type)

class BaseView(FlaskView):

  __decorators = [serialize]

  def __init__(self, *args, **kwargs):
    super(BaseView, self).__init__(*args, **kwargs)

  @class_property
  def decorators(cls):
    return cls.__decorators

  @decorators.setter
  def decorators(cls, decorator):
    cls.__decorators.insert(0, decorator)
