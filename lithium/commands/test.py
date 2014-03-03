import nose

from flask.ext.script import Command, Option


class TestCommand(Command):
  "Using nosetests, test them all!!!"

  def __init__(self, package, *args, **kwargs):
    super(TestCommand, self).__init__(*args, **kwargs)
    self.packages = package

  option_list = (
      Option('--with-notify', '-wn', dest='notify'),
  )

  def run(self, notify):
    cover = ""
    for package in self.packages:
      cover += "--cover-package=%s " % package

    basic_nose_argv = ["tests=tests", "--with-coverage",
                       cover]

    nose.main(argv=basic_nose_argv)
