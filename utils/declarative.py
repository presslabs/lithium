from sqlalchemy.ext.declarative import declarative_base

from flask.ext.sqlalchemy import SQLAlchemy, _BoundDeclarativeMeta, _QueryProperty, Model

class ValidationModel(Model):

  @property
  def valid(self):
    self.errors = {}

    for attr in dir(self):
      if attr.startswith('validate_'):
        validate_attr = attr[9:]

        field_validation = getattr(self, attr)(self, validate_attr)

        if field_validation is not True:
          if validate_attr not in self.errors:
            self.errors[validate_attr] = []

          self.errors[validate_attr] += field_validation

    return True if not self.errors else False

class BaseSQLAlchemy(SQLAlchemy):

  def make_declarative_base(self):
    """Creates the declarative base."""
    base = declarative_base(cls=ValidationModel, name='Model',
                            metaclass=_BoundDeclarativeMeta)
    base.query = _QueryProperty(self)
    return base
