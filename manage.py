from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from plutonium import create_app
from utils.commands import TestCommand, database

if __name__ == "__main__":
  manager = Manager(create_app)

  manager.add_option('-c', '--config', dest='config', required=False)
  manager.add_command('test', TestCommand())
  manager.add_command('database', database)
  manager.add_command('migration', MigrateCommand)

  manager.run()
