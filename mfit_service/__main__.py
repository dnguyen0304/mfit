# -*- coding: utf-8 -*-

import sys

import mfit_service
from mfit_service import manage
from mfit_service import services
from mfit_service import utilities


if __name__ == '__main__':

    try:
        if sys.argv[1] == 'test':
            manage.run_test_suite()
    except IndexError:
        if mfit_service.configuration['environment'] == utilities.Environment.Production.name:
            services.app.run()
        else:
            services.app.run(debug=True)

