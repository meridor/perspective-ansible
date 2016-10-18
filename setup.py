#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('lib'))
try:
    from setuptools import setup, find_packages
except ImportError:
    print("perspective-ansible needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

setup(name='perspective-ansible',
      version=1.0,
      description='Radically simple IT automation',
      author='Meridor',
      author_email='support@meridor.org',
      url='http://meridor.org/perspective',
      license='Apache 2.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Installation/Setup',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
      ],
      scripts=['perspective-inventory']
      )
