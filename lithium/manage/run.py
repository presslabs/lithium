import argh
import argparse
from lithium.manage.commands import new

parser = argh.ArghParser()
parser.add_commands([new])

def main():
  parser.dispatch()

if __name__ == "__main__":
  main()
