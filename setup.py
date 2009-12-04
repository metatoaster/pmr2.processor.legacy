from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='pmr2.processor.legacy',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Tommy Yu',
      author_email='tommy.yu@auckland.ac.nz',
      url='http://www.cellml.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pmr2', 'pmr2.processor'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'lxml>2.0.5',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
