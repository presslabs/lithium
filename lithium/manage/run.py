import argh
import argparse
from lithium.manage.commands import new
from lithium.manage.commands.clients import client

parser = argh.ArghParser()
parser.add_commands([new, client])

def main():
  parser.dispatch()

if __name__ == "__main__":
  main()
