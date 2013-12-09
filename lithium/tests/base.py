from flask.ext.testing import TestCase

class BaseTest(TestCase):
  app = None

  def setUp(self):
    self.db.create_all()

  def tearDown(self):
    self.db.session.remove()
    self.db.drop_all()
