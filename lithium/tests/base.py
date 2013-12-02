from flask.ext.testing import TestCase

class BaseTest(TestCase):
  app = None
  db = None

  def create_app(self):
    return self.app('local_config.py')

  def setUp(self):
    self.db.create_all()

  def tearDown(self):
    self.db.session.remove()
    self.db.drop_all()
