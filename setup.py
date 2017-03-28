#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    project_name = 'mfit'

    description = 'A modern health and fitness application driven by "you" data.'

    with open('./README.md', 'r') as file:
        long_description = file.read()

    install_requires = list()

    setuptools.setup(name=project_name,
                     version='1.0.0',
                     description=description,
                     long_description=long_description,
                     url='https://github.com/dnguyen0304/mfit.git',
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)
