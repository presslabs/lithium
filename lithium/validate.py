from lithium.validators.exceptions import ValidationException

class Validate(object):

  def __init__(self, *args):
    self.validators = args
    self.errors = []

  def __call__(self, obj, attr):
    self.errors = []

    if not getattr(obj, attr, None):
      self.errors.append("%s field not found in request" % attr)
      return self.errors

    for validator in self.validators:
      try:
        validator(obj, attr)
      except ValidationException as e:
        self.errors.append(e.message)

    if self.errors:
      return self.errors

    return True
