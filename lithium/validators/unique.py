from utils.validators.validator import Validator
from utils.validators.exceptions import ValidationException

class Unique(Validator):

  def validate(self, model, attr):
    if getattr(model, 'id', None): return True

    class_attr = getattr(model.__class__, attr)
    items = model.__class__.query.filter(class_attr==getattr(model, attr)).all()

    if items:
      raise ValidationException("%s is not unique" % attr)

    return True
