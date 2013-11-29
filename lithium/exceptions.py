from werkzeug.exceptions import HTTPException
from werkzeug.utils import escape

from utils.views.base import serialize_response, get_request_type

class BaseHttpException(HTTPException):

  _template = {
    'json': {
      'description': lambda description: description,
      'headers': ('Content-Type', 'application/json'),
      'body': lambda code, name, description: description,
    },
    'xml': {
      'description': lambda description: description,
      'headers': ('Content-Type', 'application/xml'),
      'body': lambda code, name, description: description,
    },
    'html': {
      'description': lambda description: u'<p>%s</p>' % escape(description),
      'headers': ('Content-Type', 'application/json'),
      'body': lambda code, name, description: (
            u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
            u'<title>%(code)s %(name)s</title>\n'
            u'<h1>%(name)s</h1>\n'
            u'%(description)s\n'
        ) % {
            'code':         code,
            'name':         name,
            'description':  description
        }
    }
  }

  def __init__(self, description=None, response=None):
    self.request_type = get_request_type()
    description = serialize_response(self.request_type, description)

    super(BaseHttpException, self).__init__(description, response)

  def get_description(self, environ=None):
    """Get the description."""
    print self.request_type
    return self._template[self.request_type]['description'](self.description)

  def get_body(self, environ=None):
    """Get the body"""
    return self._template[self.request_type]['body'](self.code, escape(self.name), self.get_description(environ))

  def get_headers(self, environ=None):
    """Get a list of headers."""
    return [self._template[self.request_type]['headers']]

class HttpBadRequest(BaseHttpException):
  code = 400

class HttpUnauthorized(BaseHttpException):
  code = 401

class HttpPaymentRequired(BaseHttpException):
  code = 402

class HttpForbidden(BaseHttpException):
  code = 403

class HttpNotFound(BaseHttpException):
  code = 404

class HttpMethodNotAllowed(BaseHttpException):
  code = 405
