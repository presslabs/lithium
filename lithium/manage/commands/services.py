from random import randint
from os import listdir, chdir, makedirs
from os.path import isdir, join, dirname, abspath

from argh.decorators import arg
from jinja2 import Template
import yaml
from colorama import Fore

from elements import all

help = "Bootstrap a service with all you need"
@arg('name', default=all[randint(0, len(all))], help=help)
def new(name):
  working_dir = dirname(abspath(__file__)) + '/..'
  print working_dir

  print Fore.BLUE + "\nCreating service folder..."
  makedirs(name)
  print Fore.CYAN + "Done!\n"

  with open('%s/layouts/default.yml' % working_dir) as f:
    layout = yaml.load(Template(f.read()).render(app_name=name))
    print Fore.RED + "Creating layout..."
    create_service(1, layout, '%s/templates' % working_dir, name, name)

  print Fore.BLUE + "\nYou're service layout is ready" + Fore.RESET
  return ""

def create_service(deep, layout, templates_dir, current_dir, app_name):
  for item in layout:
    if isinstance(item, dict):
      path = "%s/%s" % (current_dir, item.keys()[0])
      makedirs(path)
      print Fore.BLUE + "  "*deep + "|- %s/" % item.keys()[0]
      create_service(deep+1, item[item.keys()[0]], templates_dir, path, app_name)
    elif item.endswith("/"):
      path = "%s/%s" % (current_dir, item)
      makedirs(path)
      print Fore.BLUE + "  "*deep + "|- %s/" % item
    else:
      with open("%s/%s" % (templates_dir, item)) as f:
        content = f.read()
        template = Template(content)
        content = template.render(app_name=app_name)
      with open("%s/%s" % (current_dir, item), 'w') as f:
        f.write(content)
        print Fore.CYAN + "  "*deep + "|- %s" % item
