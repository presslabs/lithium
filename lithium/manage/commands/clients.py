import os
import uuid

from argh.decorators import arg
from colorama import Fore
import yaml

def generate():
  "Generate a client_id and a client_key"

  client_id = "%s" % uuid.uuid4()
  client_key = os.urandom(16).encode("base64")[:21]

  print '\n'+ Fore.YELLOW + "Client id: " + Fore.GREEN + client_id + Fore.RESET
  print Fore.YELLOW + "Client key: " + Fore.GREEN + client_key + Fore.RESET + '\n'
