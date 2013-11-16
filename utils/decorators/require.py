import requests
from functools import wraps

from flask import request, current_app

from utils.decorators.signature import sign

def require(resource_namespace, permissions, resource_id=None):
  def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      if request.method == 'GET':
        payload = request.args

      client_key = current_app.config['CLIENTS']['plutonium']['client_key']
      client_id = current_app.config['CLIENTS']['plutonium']['client_id']

      data = []
      for permission in permissions:
        data.append({
          'client_namespace'   : 'app',
          'client_id'          : payload['client_id'],
          'resource_namespace' : resource_namespace,
          'permission'         : permission,
          'resource_id'        : resource_id or '*'
        })

      result = f(*args, **kwargs)
      return result
    return decorated_function

  return decorator
