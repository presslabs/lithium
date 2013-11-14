import time

from werkzeug import generate_password_hash, check_password_hash

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from utils.validate import Validate
from utils.validators import Unique, Lenght, Email

from todoapi.extensions import db

class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)

  username = db.Column(db.String(80), unique=True)
  validate_username = Validate(Unique(), Lenght(6, 12))

  email = db.Column(db.String(120), unique=True)
  validate_email = Validate(Unique(), Lenght(6, 120), Email())

  first_name = db.Column(db.String(80), nullable=False)
  validate_first_name = Validate(Lenght(4, 80))

  last_name = db.Column(db.String(80))
  validate_last_name = Validate(Lenght(4, 80))

  created = db.Column(db.Integer, default=int(time.time()))
  last_modified = db.Column(db.Integer, onupdate=int(time.time()), nullable=True)

  _password = db.Column('password', db.String(80), nullable=False)

  def _get_password(self):
    return self._password

  def _set_password(self, password):
    self._password = generate_password_hash(password)

  # Hide password encryption by exposing password field only.
  password = db.synonym('_password',
                        descriptor=property(_get_password,
                                            _set_password))
  validate_password = Validate(Lenght(6, 80))

  def check_password(self, password):
    if self.password is None:
      return False
    return check_password_hash(self.password, password)

  def __repr__(self):
    return '<User %r>' % self.username
