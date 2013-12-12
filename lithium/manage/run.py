import argh
import argparse
from lithium.manage.commands.services import new
from lithium.manage.commands.clients import generate

parser = argh.ArghParser()
parser.add_commands([new], namespace='service', title='Services related commands')
parser.add_commands([generate], namespace='client', title='Clients related commands')

def main():
  parser.dispatch()

if __name__ == "__main__":
  main()
