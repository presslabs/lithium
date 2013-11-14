import json

from nose.tools import eq_

from plutonium.users.tests.base_tests import TestWithUser
from plutonium.users.models import User

from utils.tests import fixtures

load_fixture = fixtures('users', 'user.retrieve')

class UserRetrieveTest(TestWithUser):
  '''
    Try to cover all get user use cases
  '''

  def test_user_get_with_valid_data(self):
    '''
      Basic get user
    '''

    response = self.client.get("/api/1/users/1", content_type='application/json')

    assert_response = load_fixture('simple_user')
    assert_response['created'] = User.query.get(1).created

    eq_(response.data, json.dumps(assert_response))

  def test_user_index_with_valid_data(self):
    '''
      Get all users
    '''

    response = self.client.get("/api/1/users/", content_type='application/json')

    assert_response = load_fixture('index')
    assert_response[0]['created'] = User.query.get(1).created

    eq_(response.data, json.dumps(assert_response))

  def test_user_missing_item(self):
    '''
      Try to retrieve a non-existing item from database
    '''

    response = self.client.get("/api/1/users/2", content_type='application/json')

    assert_response = load_fixture('missing_user')

    eq_(response.data, json.dumps(assert_response))
