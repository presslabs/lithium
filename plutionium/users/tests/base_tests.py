from utils.tests.fixtures import fixtures
from utils.tests.base import BaseTest

from todoapi.extensions import db
from todoapi.users.models import User

class TestWithUser(BaseTest):

  def setUp(self):
    super(TestWithUser, self).setUp()
    data = fixtures('users', 'user.create')('create_user_valid_data')

    user = User(**data)

    db.session.add(user)
    db.session.commit()
