#!/usr/bin/env python
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from {{ app_name }} import create_app
from {{ app_name }}.extensions import db
from lithium.commands import TestCommand, database

if __name__ == "__main__":
  manager = Manager(create_app)

  manager.add_option('-c', '--config', dest='config', required=False)
  manager.add_command('test', TestCommand(package="{{ app_name }}"))
  manager.add_command('database', database(db))
  manager.add_command('migration', MigrateCommand)

  manager.run()
