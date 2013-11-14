import json

from nose.tools import eq_

from todoapi.users.models import User

from utils.tests.base import BaseTest
from utils.tests import fixtures

load_fixture = fixtures('users', 'user.create')

class UserCreationTest(BaseTest):
  '''
    Try to cover all user creation use cases
  '''

  def test_user_creation_with_valid_data(self):
    '''
      Basic user creation with valid data
    '''
    data = load_fixture('create_user_valid_data')
    response = self.client.post("/api/1/users/", data=json.dumps(data),
                                content_type='application/json')

    assert_response = load_fixture('response_valid_data')
    assert_response['created'] = User.query.get(1).created

    eq_(json.loads(response.data), assert_response)
    eq_(response.status_code, 200)

  def test_user_with_missing_params(self):
    '''
      If you want to create a user, you have to pass some required params, like
      username, password, first_name, last_name, email.
      When you forget one or more params, the api will return a 400 (Bad request)
    '''

    data = load_fixture('create_user_missing_data')
    response = self.client.post("/api/1/users/", data=json.dumps(data),
                                content_type='application/json')

    assert_response = load_fixture('response_missing_data')

    eq_(response.data, json.dumps(assert_response))
    eq_(response.status_code, 400)

  def test_user_with_invalid_params(self):
    '''
      Test data validation, passing invalid email
    '''

    data = load_fixture('create_user_invalid_email')
    response = self.client.post("/api/1/users/", data=json.dumps(data),
                                content_type='application/json')

    assert_response = load_fixture('response_invalid_email')
    eq_(response.data, json.dumps(assert_response))
    eq_(response.status_code, 400)
