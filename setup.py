from setuptools import setup, find_packages

requires = ['pyyaml>=3.1', 'colorama>=0.2.5', 'Jinja2>=2.7.1', 'MarkupSafe>=0.18',
            'argcomplete>=0.6.3', 'argparse>=1.2.1', 'wsgiref>=0.1.2', 'argh==0.23.3']

setup(name="lithum",
      version="0.1.4",
      platforms='any',
      packages = find_packages(),
      include_package_data=True,
      install_requires=requires,
      author = "Vlad Temian",
      author_email = "vlad@presslabs.com",
      url = "https://github.com/Presslabs/lithium",
      description = "Flask goodies",
      entry_points = {'console_scripts': [ 'lithium = lithium.manage.run:main' ]},
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
      ]
)
