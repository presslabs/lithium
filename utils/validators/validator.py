from abc import ABCMeta, abstractmethod

class Validator(object):

  __metaclass__ = ABCMeta

  def __call__(self, model, attr):
    return self.validate(model, attr)

  @abstractmethod
  def validate(self):
    raise NotImplemented('This method must be implemented')
