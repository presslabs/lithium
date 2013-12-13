import os
import uuid

import yaml
import redis
from argh.decorators import arg
from colorama import Fore

@arg('file', help="Import a list of clients from a yml file into redis")
def import_data(file):
  #TODO: check for yaml_file
  with open(file) as yaml_file:
    clients = yaml.load(yaml_file.read())

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    for client in clients:
      for username in client:
        data = client[username]
        data['id'] = '%s' % uuid.uuid4()
        del data['permissions']

        redis_client.hmset('apqu:users:%s' % username, data)
        redis_client.set('apqu:users:by_id:%s' % data['id'], username)
