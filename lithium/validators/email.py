from lithium.validators.validator import Validator
from lithium.validators.exceptions import ValidationException

class Email(Validator):

  def validate(self, model, attr):
    value = getattr(model, attr)

    if '@' not in value:
      raise ValidationException("Invalid email")

    return True
