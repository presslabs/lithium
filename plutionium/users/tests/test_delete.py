import json

from nose.tools import eq_

from utils.tests.fixtures import fixtures
from todoapi.users.tests.base_tests import TestWithUser

load_fixture = fixtures('users', 'user.delete')

class UserDeleteTest(TestWithUser):
  '''
    Try to cover all user deletion use cases
  '''

  def test_user_deletion_with_valid_data(self):
    '''
      Basic user removal
    '''

    response = self.client.delete("/api/1/users/1", content_type='application/json')

    assert_response = load_fixture('success')

    eq_(response.data, json.dumps(assert_response))

  def test_user_deletion_with_missing_user(self):
    '''
      Try to remove a non-existing user
    '''

    response = self.client.delete("/api/1/users/2", content_type='application/json')

    assert_response = load_fixture('missing')

    eq_(response.data, json.dumps(assert_response))
