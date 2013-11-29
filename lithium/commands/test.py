import nose

from flask.ext.script import Command, Option

class TestCommand(Command):
  "Using nosetests, test them all!!!"

  option_list = (
    Option('--with-notify', '-wn', dest='notify'),
  )

  def run(self, notify):
    basic_nose_argv = ["tests=tests", "--with-coverage",
                       "--cover-package=plutonium"]

    nose.main(argv=basic_nose_argv)
