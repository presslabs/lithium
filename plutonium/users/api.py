from flask import request
from flask.ext.classy import  route

from utils.views import ModelView
from utils.decorators import require, signature

from plutonium.users.models import User

class UsersView(ModelView):
  model = User
  __exclude__ = ['password']

  @route('/filter/', methods=['GET'])
  @signature
  @require('users', ['get_user_by_username'], resource_id=1)
  def filter(self):
    return "yeye"
