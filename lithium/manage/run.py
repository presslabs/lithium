import argh
import argparse
from lithium.manage.commands.services import new
from lithium.manage.commands.clients import generate
from lithium.manage.commands.users import import_data

parser = argh.ArghParser()
parser.add_commands([new], namespace='service', title='Services related commands')
parser.add_commands([generate], namespace='client', title='Clients related commands')
parser.add_commands([import_data], namespace='user', title='Users related commands')

def main():
  parser.dispatch()

if __name__ == "__main__":
  main()
