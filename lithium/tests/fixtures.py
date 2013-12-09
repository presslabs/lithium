import yaml
from unipath import Path

def fixtures_wrapper(app_name):

  def fixtures(module, yaml_file):

    yaml_file = Path.cwd().child(app_name, module, 'tests', 'fixtures', '%s.yml' % yaml_file)

    with open(yaml_file) as yaml_file:
      fixtures = yaml.load(yaml_file.read())

    def load_fixture(fixture_name):
      if fixture_name in fixtures:
        return fixtures[fixture_name]
      else:
        raise LookupError('%s doesnt exists in this fixture file' % fixture_name)

    return load_fixture
  return fixtures
