from lithium.validators.exceptions import ValidationException, StopValidation

class Validate(object):

  def __init__(self, *args):
    self.validators = args
    self.errors = []

  def __call__(self, obj, attr):
    self.errors = []

    for validator in self.validators:
      try:
        validator(obj, attr)
      except ValidationException as e:
        self.errors.append(e.message)
      except StopValidation as e:
        self.errors.append(e.message)
        return self.errors

    if self.errors:
      return self.errors

    return True
