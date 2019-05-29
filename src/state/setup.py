#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import setup, find_packages

VERSION = "0.0.1"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = []

setup(
    name='state-extension',
    version=VERSION,
    description='Support for tenant-wide governance querying.',
    long_description='Support for tenant-wide querying of custom role and policy definitions, role and policy assignments, locks, and your resource hierarchy.',
    license='MIT',
    author='Bennett Battistoni',
    author_email='bebattis@microsoft.com',
    url='https://github.com/bebattis/azure-cli-extensions',
    classifiers=CLASSIFIERS,
    package_data={'azext_state': ['azext_metadata.json']},
    packages=find_packages(),
    install_requires=DEPENDENCIES
)
