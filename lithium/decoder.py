class AlchemyDecoder(dict):

  def __init__(self, model, ignore=None):
    model_dict = self.__model_to_dict__(model, ignore)
    super(AlchemyDecoder, self).__init__(**model_dict)

  def __model_to_dict__(self, model, ignore):
    result = {}

    if not ignore:
      ignore = []

    for key in model.__mapper__.c.keys():
      if key not in ignore and not key.startswith('_'):
        result[key] = getattr(model, key)

    return result
