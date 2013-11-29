from utils.declarative import BaseSQLAlchemy as SQLAlchemy
db = SQLAlchemy()

from flask.ext.cache import Cache
cache = Cache()

from flask.ext.admin import Admin
admin = Admin(name='{{app_name}}')

from flask.ext.migrate import Migrate, MigrateCommand
migrate = Migrate()
