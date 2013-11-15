from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from plutonium import create_app
from plutonium.config import HOST, PORT

from utils.commands import TestCommand, database

if __name__ == "__main__":
  manager = Manager(create_app)

  manager.add_option('-c', '--config', dest='config', required=False)
  manager.add_command('test', TestCommand())
  manager.add_command('database', database)
  manager.add_command('migration', MigrateCommand)

  server = Server(host=HOST, port=PORT)
  manager.add_command("runserver", server)

  manager.run()
