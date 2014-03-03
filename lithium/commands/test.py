import nose

from flask.ext.script import Command, Option


class TestCommand(Command):
  "Using nosetests, test them all!!!"

  def __init__(self, packages, *args, **kwargs):
    super(TestCommand, self).__init__(*args, **kwargs)
    self.packages = packages

  option_list = (
      Option('--with-notify', '-wn', dest='notify'),
  )

  def run(self, notify):
    basic_nose_argv = ["tests=tests", "--with-coverage"]
    for package in self.packages:
      basic_nose_argv .append("--cover-package=%s" % package)

    nose.main(argv=basic_nose_argv)
