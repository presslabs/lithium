import json
import hmac
import hashlib
from functools import wraps

from flask import request, current_app

from utils.exceptions import HttpUnauthorized, HttpForbidden

def signature(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if request.method == 'GET':
      payload = request.args

    key = get_key(payload['client_id'])
    signature = sign(payload['data'], key)

    if signature != payload['signature']:
      raise HttpUnauthorized('Invalid signature')

    result = f(*args, **kwargs)
    return result

  return decorated_function

def sign(message, key):
  if not isinstance(message, unicode) and not isinstance(message, str):
    message = json.dumps(message)
  return hmac.new(key, message, hashlib.sha1).hexdigest()

def get_key(client_id):
  for client_name, client in current_app.config['CLIENTS'].iteritems():
    if 'client_id' in client and client['client_id'] == client_id:
      return client['client_key']

  raise HttpForbidden("Invalid client id")
