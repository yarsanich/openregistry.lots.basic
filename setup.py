from setuptools import setup, find_packages
import os

version = '0.1.dev0'

entry_points = {
    'openregistry.lots.core.plugins': [
        'lots.basic = openregistry.lots.basic.includeme:includeme'
    ],
    'openregistry.tests': [
        'lots.basic = openregistry.lots.basic.tests.main:suite'
    ]
}

requires = [
    'setuptools',
    'openregistry.lots.core'
]

setup(name='openregistry.lots.basic',
      version=version,
      description="",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      url='https://github.com/openprocurement/openregistry.lots.basic',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openregistry', 'openregistry.lots'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points=entry_points,
      )
