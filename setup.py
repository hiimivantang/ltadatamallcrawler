#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'requests',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ltadatamallcrawler',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A package that gets traffic data from LTA datamall APIs.",
    long_description=readme + '\n\n' + history,
    author="Ivan Tang",
    author_email='hiimivantang@gmail.com',
    url='https://github.com/hiimivantang/ltadatamallcrawler',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    #package_data={
    #  'ltadatamallcrawler':['urls.csv','settings.yaml']
    #},
    entry_points={
        'console_scripts':[
            'lta-datamall-crawler=ltadatamallcrawler.requestor:main',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="GPL",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
