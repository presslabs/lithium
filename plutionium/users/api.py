from utils.views import ModelView

from todoapi.users.models import User

class UsersView(ModelView):
  model = User
  __exclude__ = ['password']
