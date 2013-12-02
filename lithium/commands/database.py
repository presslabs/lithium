import nose

from colorama import Fore, Back, Style
from flask.ext.script import Command, Option, Manager, prompt_bool

def database(db):
  manager = Manager(usage="Perform database operations")

  @manager.command
  def drop():
    "Drops database tables"

    if prompt_bool(Fore.YELLOW + "Are you sure you want to lose all your data" + Fore.RESET):
      db.drop_all()
      print Fore.GREEN + "Done!" + Fore.RESET

  @manager.command
  def create():
    "Creates database tables"

    db.create_all()
    print Fore.GREEN + "Done!" + Fore.RESET

  @manager.command
  def sync():
    "Drop database and create new one"

    if prompt_bool(Fore.YELLOW + "Are you sure you want to lose all your data" + Fore.RESET):
      print Fore.RED + "Droping database..." + Fore.RESET
      db.drop_all()
      print Fore.RED + "Creating new database..." + Fore.RESET
      db.create_all()
      print Fore.GREEN + "Done!" + Fore.RESET

  return manager
