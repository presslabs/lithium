import json

from utils.declarative import BaseSQLAlchemy as SQLAlchemy
db = SQLAlchemy()

from flask.ext.cache import Cache
cache = Cache()

from flask.ext.admin import Admin
admin = Admin(name='TodoAPI')

from flask_oauthlib.provider import OAuth1Provider
oauth = OAuth1Provider()

from flask.ext.migrate import Migrate, MigrateCommand
migrate = Migrate()
