#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import shutil
import site
import sys

if __name__ == '__main__':
    project_name = 'mfit_service'

    with open('./README.md', 'r') as file:
        long_description = file.read()

    with open('./requirements.txt', 'r') as file:
        install_requires = file.read().splitlines()

    setuptools.setup(name=project_name,
                     version='0.1',
                     description='',
                     long_description=long_description,
                     url='https://github.com/dnguyen0304/{}.git'.format(project_name),
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     packages=[project_name,
                               project_name + '.models',
                               project_name + '.repositories',
                               project_name + '.services'],
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True,
                     zip_safe=False)

    # The configuration file needs to be included because the code
    # relies on relative paths.
    reload(site)

    if sys.argv[1] == 'install':
        for path in sys.path:
            if 'site-packages' in path and project_name in path:
                shutil.copy2('project.config', path)
                break

