import json

from nose.tools import eq_

from utils.tests.fixtures import fixtures

from todoapi.users.models import User
from todoapi.users.tests.base_tests import TestWithUser

load_fixture = fixtures('users', 'user.update')

class UserUpdateTest(TestWithUser):
  '''
    Try to cover all user update use cases
  '''

  def test_user_update_with_valid_data(self):
    '''
      Basic task update
    '''

    data = load_fixture('update_user_valid_data')

    response = self.client.put("/api/1/users/1", data=json.dumps(data),
                              content_type='application/json')

    data = load_fixture('response_valid_data')
    data['last_modified'] = User.query.get(1).last_modified
    data['created'] = User.query.get(1).created

    eq_(json.loads(response.data), data)

  def test_user_update_with_missing_user(self):
    '''
      Update a non-existing user
    '''

    data = {}

    response = self.client.put("/api/1/users/2", data=json.dumps(data),
                              content_type='application/json')

    data = load_fixture('non_existing_user')
    eq_(json.loads(response.data), data)

  def test_user_with_invalid_params(self):
    '''
      Test data validation, passing invalid email
    '''

    data = load_fixture('update_user_invalid_email')
    response = self.client.put("/api/1/users/1", data=json.dumps(data),
                                content_type='application/json')

    assert_response = load_fixture('response_invalid_email')
    eq_(response.data, json.dumps(assert_response))
    eq_(response.status_code, 400)
