import json
import requests
from functools import wraps

from flask import request, current_app

from utils.decorators.signature import sign
from utils.exceptions import HttpUnauthorized

def require(resource_namespace, permissions, resource_id=None):
  def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      if request.method == 'GET':
        payload = request.args

      client_key = current_app.config['CLIENTS']['plutonium']['client_key']
      client_id = current_app.config['CLIENTS']['plutonium']['client_id']
      apq = current_app.config['CLIENTS']['apq']

      data = []
      for permission in permissions:
        data.append({
          'client_namespace'   : 'app',
          'client_id'          : payload['client_id'],
          'resource_namespace' : resource_namespace,
          'permission'         : permission,
          'resource_id'        : resource_id or '*'
        })

      signature = sign(client_key, json.dumps(data))
      payload = {
        'data'     : json.dumps(data),
        'client_id': client_id,
        'signature': signature
      }

      apq = requests.get("http://%s/has_perm" % apq['host'], params=payload)

      permission = json.loads(apq.content)
      granted = [granted for granted in permission if granted == 'True']

      if len(permission) != len(granted):
        raise HttpUnauthorized("You don't have enough permission to access this resource")

      result = f(*args, **kwargs)
      return result

    return decorated_function

  return decorator
