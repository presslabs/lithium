from flask.ext.classy import  route

from utils.views import ModelView

from plutonium.users.models import User

class UsersView(ModelView):
  model = User
  __exclude__ = ['password']

  @route('/filter/')
  def filter(self):
    return "yeye"
