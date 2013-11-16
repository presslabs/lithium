from functools import wraps

def require(*permissions):

  def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      result = f(*args, **kwargs)
      return result
    return decorated_function

  return decorator
