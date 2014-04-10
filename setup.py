#!/usr/bin/env python

from distutils.core import setup

setup(name='pfc-libs',
      version='1.0',
      description='Configure postfix main.cf and master.cf from snippets',
      long_description='Configure postfix main.cf and master.cf from snippets',
      author='Stefan Neben',
      author_email='stefan.neben@gmail.com',
      license="GPLv3",
      url='https://github.com/sneben/postfix-configurator',
      packages=['pfc'],
      package_dir={'pfc': 'lib'})
