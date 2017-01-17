# -*- coding: utf-8 -*-

import collections

from mfit import app
from mfit import models
from mfit import resources


class AttemptsLogsCollection(resources.BaseCollection):

    _model = models.AttemptsLogs
    _resource = resources.AttemptsLogs

    def get(self, attempts_id):
        data = [self._resource.get_self_link(entity=attempts_log)
                for attempts_log
                in self._db_context.query(self._model).all()]

        links = {
            'self': app.api.url_for(AttemptsLogsCollection,
                                    attempts_id=attempts_id,
                                    _external=True)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

    def post(self, attempts_id):
        return super().post()


AttemptsLogsCollection._resource_collection = AttemptsLogsCollection

