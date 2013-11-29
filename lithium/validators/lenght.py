from utils.validators.validator import Validator
from utils.validators.exceptions import ValidationException

class Lenght(Validator):

  def __init__(self, min, max):
    self.min = min
    self.max = max

  def validate(self, model, attr):
    value = getattr(model, attr)

    if len(value) < self.min or len(value) > self.max:
      raise ValidationException("This field has to be between %s and %s" % (self.min, self.max))

    return True
