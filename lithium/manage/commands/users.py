import os
import uuid

from argh.decorators import arg
from colorama import Fore
import yaml

@arg('file', help="Import a list of clients from a yml file into redis")
def import_data(file):
  #TODO: check for yaml_file
  with open(file) as yaml_file:
    clients = yaml_file.read()

    redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    for client in clients:
      hash = 'apqu:permissions:%s:%s' % (client['client_id'], client['client_key'])
      #redis.hset( )
