import os
from importlib import import_module

from flask import Flask
from flask.ext.admin.contrib.sqla import ModelView as AdminModelView

from {{app_name}}.extensions import db, admin, migrate

from lithium.views import ModelView

cache = []

def create_app(config=None):

  app = Flask(__name__)

  default_config = os.path.join(app.root_path, 'config.py')
  app.config.from_pyfile(default_config)

  if config:
    app.config.from_pyfile(config)

  blueprints = []

  db.init_app(app)

  admin_panel = register_admin_views(admin, blueprints)
  admin_panel.init_app(app)

  app = register_endpoints(app, blueprints)

  migrate.init_app(app, db)

  return app

def register_admin_views(admin, blueprints):

  for module in blueprints:
    module = import_module('{{app_name}}.%s.models' % module)

  for model in db.Model.__subclasses__():
    if model not in cache:
      cache.append(model)
      admin.add_view(AdminModelView(model, db.session))

  return admin

def register_endpoints(app, blueprints):

  for module in blueprints:
    module = import_module('{{app_name}}.%s.api' % module)

  for endpoint in ModelView.__subclasses__():
    endpoint.register(app, route_prefix='/api/1/')

  return app
