from lithium.validators.validator import Validator
from lithium.validators.exceptions import StopValidation

class Required(Validator):

  def validate(self, model, attr):
    if getattr(model, attr, None) is None:
      raise StopValidation('This field was not found in request')

    return True
