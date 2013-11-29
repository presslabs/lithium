import argh
import argparse
from commands import new

parser = argh.ArghParser()
parser.add_commands([new])

if __name__ == "__main__":
  parser.dispatch()
