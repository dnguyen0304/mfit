#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mfit
from mfit import app
from mfit import utilities


if __name__ == '__main__':
    if mfit.configuration['environment'] == utilities.Environment.Production.name:
        app.app.run()
    else:
        app.app.run(debug=True)

