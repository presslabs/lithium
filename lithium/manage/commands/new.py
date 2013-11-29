from random import randint
from os import listdir, chdir, makedirs
from os.path import isdir, join

from argh.decorators import arg
from jinja2 import Template
import yaml

from elements import all

help = "Bootstrap a service with all you need"
@arg('name', default=all[randint(0, len(all))], help=help)
def new(name):
  makedirs(name)

  with open('layouts/default.yml') as f:
    layout = yaml.load(Template(f.read()).render(app_name=name))
    create_service(layout, 'templates', name, name)

  return name

def create_service(layout, templates_dir, current_dir, app_name):
  for item in layout:
    if isinstance(item, dict):
      path = "%s/%s" % (current_dir, item.keys()[0])
      makedirs(path)
      create_service(item[item.keys()[0]], templates_dir, path, app_name)
    elif item.endswith("/"):
      path = "%s/%s" % (current_dir, item)
      makedirs(path)
    else:
      with open("%s/%s" % (templates_dir, item)) as f:
        content = f.read()
        template = Template(content)
        content = template.render(app_name=app_name)
      with open("%s/%s" % (current_dir, item), 'w') as f:
        f.write(content)
